#!/usr/bin/env

##########################################
## 
## author: errol strain, estrain@gmail.com
##
##########################################

from argparse import (ArgumentParser, FileType)
import sys
import glob
import subprocess
import json

def parse_args():
  "Parse the input arguments, use '-h' for help."

  parser = ArgumentParser(description='Run MicorRunQC on a pair of gzipped FASTQ files')

  # Read inputs
  parser.add_argument('--forward', type=str, required=True, nargs=1, help='Forward Read')
  parser.add_argument('--reverse', type=str, required=True, nargs=1, help='Reverse Read') 
  parser.add_argument('--output', type=str, required=True, nargs=1, help='Output Filenames')
  parser.add_argument('--cores', type=int, required=False, nargs=1, help='Number of cores',default=8)
  parser.add_argument('--fqtype', type=str, required=False, nargs=1, help='gzipped or unzipped',default="gz")

  return parser.parse_args()

args =parse_args()


fread=args.forward[0]
rread=args.reverse[0]
ftread=fread.replace(".fastq.",".trimmed.fastq.")
rtread=rread.replace(".fastq.",".trimmed.fastq.")


## Trimmomatic to remove zero length reads.  These cause fastq-scan to crash.
## Usually a very small number of reads, results of trimming are not reported.

cmd1 = ["trimmomatic","SE","-threads",str(args.cores),"-phred33",fread,ftread,"MINLEN:1"]
cmd2 = ["trimmomatic","SE","-threads",str(args.cores),"-phred33",rread,rtread,"MINLEN:1"]

subprocess.call(cmd1)
subprocess.call(cmd2)

## Run skesa to produce de novo assemblies

seqfiles = "".join([fread,",",rread])
contigs = "".join([args.output[0],".fasta"])
cmd = ["skesa","--fastq",seqfiles,"--contigs_out",contigs]

subprocess.call(cmd)

cmd = ["bwa","index",contigs]
subprocess.call(cmd) 


## bwa is used to get the median insert size

cmd1 = ["bwa","mem","-t",str(args.cores),contigs,fread,rread]
cmd2 = ["python","median_size.py"]

pcmd1 = subprocess.Popen(cmd1,stdout= subprocess.PIPE,shell=False)
pcmd2 = subprocess.Popen(cmd2,stdin=pcmd1.stdout,stdout=subprocess.PIPE,shell=False).communicate()[0]
insert = pcmd2.decode('utf-8')

mlstout = "".join([args.output[0],".mlst.tsv"])
cmd = ["mlst","--nopath","--threads",str(args.cores),contigs]
pcmd = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=False).communicate()[0]
mlstprofile = pcmd.decode('utf-8')
mlstprofile = mlstprofile.rstrip()
output = open(mlstout,"w")
output.write(mlstprofile)
output.close()

fqout = "".join([args.output[0],".fq"])
cmd = ["python","run_fastq_scan.py","--fastq",fread,rread,"--out",fqout,"--type",args.fqtype]
returned_value = subprocess.call(cmd)  # returns the exit code in unix

sumout = "".join([args.output[0],"_qc.txt"])
cmd = ["python","sum_mlst.py","--fasta",contigs,"--mlst",mlstout,"--med",insert,"--fqscan",fqout,"--out",sumout]
returned_value = subprocess.call(cmd) 
