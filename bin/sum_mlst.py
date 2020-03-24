#!/usr/bin/env

## Generate basic summary stats from SKESA, fastq-scan, and MLST output.
## author: errol strain, estrain@gmail.com

from argparse import (ArgumentParser, FileType)
import sys
import glob 
import subprocess
from decimal import Decimal

def parse_args():
  "Parse the input arguments, use '-h' for help."

  parser = ArgumentParser(description='Generate Basic Summary Statistics from SKESA assemblies, fastq-scan output, and MLST reports')

  # Read inputs
  parser.add_argument('--fasta', type=str, required=True, nargs=1, help='SKESA FASTA assembly')
  parser.add_argument('--mlst', type=str, required=True, nargs=1, help='MLST output')
  parser.add_argument('--fqscan', type=str, required=True, nargs=1, help='fastq-scan output')
  parser.add_argument('--med', type=str, required=True, nargs=1, help='Median Insert Size')
  parser.add_argument('--output', type=str, required=True, nargs=1, help='Output File')

  return parser.parse_args()

args =parse_args()

# FASTA file
fasta = args.fasta[0]

# Get individual and total length of contigs
cmd = ["awk", "/^>/ {if (seqlen){print seqlen}; ;seqlen=0;next; } { seqlen = seqlen +length($0)}END{print seqlen}",fasta]
seqlen = subprocess.Popen(cmd,stdout= subprocess.PIPE).communicate()[0] 
intlen = list(map(int,seqlen.splitlines()))
totlen = sum(intlen)
# Count number of contigs
numtigs = len(intlen) 

# Get coverage information from skesa fasta header
cmd1 = ["grep",">",fasta] 
cmd2 = ["cut","-f","3","-d","_"]
p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE).communicate()[0]
covdep = map(float,p2.splitlines())
covlist = [a*b for a,b in zip([float(i) for i in intlen],covdep)]
covdep = round(sum(covlist)/totlen,1)

# Calculate N50
vals = [int(i) for i in intlen]
vals.sort(reverse=True)
n50=0
for counter in range(0,len(vals)-1):
  if sum(vals[0:counter]) > (totlen/2):
    n50=vals[counter-1]
    break

# Read in MLST output
mlst = open(args.mlst[0],"r")
profile = mlst.readline()
els = profile.split("\t")

# Read in median insert size
insert = args.med[0]

# Read in fastq-scan
fqfile = open(args.fqscan[0],"r")
fq = fqfile.readline()
fq = fq.rstrip()

output = open(args.output[0],"w")

filehead = str("File\tContigs\tLength\tEstCov\tN50\tMedianInsert\tMeanLength_R1\tMeanLength_R2\tMeanQ_R1\tMeanQ_R2\tScheme\tST\n")
output.write(filehead)

output.write(str(fasta) + "\t" + str(numtigs) + "\t" + str(totlen) + "\t" + str(covdep) + "\t" + str(n50) +"\t" + str(insert) + "\t" + str(fq))
for counter in range(1,len(els)):
  output.write("\t" + str(els[counter]))
