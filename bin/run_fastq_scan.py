#!/usr/bin/env

## Run fastq-scan to get mean read length and mean quality score  
## author: errol strain, estrain@gmail.com

from argparse import (ArgumentParser, FileType)
import sys
import glob 
import subprocess
import json

def parse_args():
  "Parse the input arguments, use '-h' for help."

  parser = ArgumentParser(description='Run fastq-scan on a pair of gzipped FASTQ files')

  # Read inputs
  parser.add_argument('--fastq', type=str, required=True, nargs=2, help='FASTQ files')
  parser.add_argument('--output', type=str, required=True, nargs=1, help='Output File')
  parser.add_argument('--type', type=str, required=True, nargs=1, help='File Type (text or gz)')

  return parser.parse_args()

args =parse_args()

# FASTA file
r1 = args.fastq[0]
r2 = args.fastq[1]

# Read 1 
if str(args.type[0]) == "gz" :
  cmd1 = ["zcat", r1]
else :
  cmd1 = ["cat", r1]
cmd2 = ["fastq-scan"]
pcmd1= subprocess.Popen(cmd1,stdout= subprocess.PIPE,shell=False)
r1json = json.loads(subprocess.Popen(cmd2, stdin=pcmd1.stdout,stdout=subprocess.PIPE,shell=False).communicate()[0])
r1q = round(r1json["qc_stats"]["qual_mean"],1)
r1l = round(r1json["qc_stats"]["read_mean"],1)

# Read 2
if str(args.type[0]) == "gz" :
  cmd1 = ["zcat", r2]
else :
  cmd1 = ["cat", r2]
cmd2 = ["fastq-scan"]
pcmd1= subprocess.Popen(cmd1,stdout= subprocess.PIPE,shell=False)
r2json = json.loads(subprocess.Popen(cmd2, stdin=pcmd1.stdout,stdout=subprocess.PIPE,shell=False).communicate()[0])
r2q = round(r2json["qc_stats"]["qual_mean"],1)
r2l = round(r2json["qc_stats"]["read_mean"],1)

# Write output to be used by sum_mlst.py
output = open(args.output[0],"w")
output.write(str(r1l) + "\t" + str(r2l) + "\t" + str(r1q) + "\t" + str(r2q))
