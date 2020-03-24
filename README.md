# MicroRunQC
Generate Metrics and Summary Statistics for paired-end Illumina Bacterial Whole-Genome Sequencing (WGS) fastq data. The pipeline was originally developed on the [Galaxy](https://galaxyproject.org/) platform and the workflow is made available.  

## Galaxy installation and setup

Install tools below from the [Galaxy Tool Shed](https://toolshed.g2.bx.psu.edu/) 
* trimmomatic
* microrunqc

Import the [MicroRunQC](https://github.com/estrain/MicroRunQC/blob/master/galaxy_workflows/MicroRunQC.ga) workflow. 

## Dependencies for local installation

* [SKESA](https://github.com/ncbi/SKESA)
  * Strategic k-mer extension for scrupulous assemblies
* [mlst](https://github.com/tseemann/mlst)
  * Scan contig files against traditional PubMLST typing schemes
* [trimmomatic](https://github.com/timflutre/trimmomatic)
  * A flexible read trimming tool for Illumina NGS data
* [bwa](https://github.com/lh3/bwa)
  * BWA is a software package for mapping DNA sequences against a large reference genome, such as the human genome
* [fastq-scan](https://github.com/rpetit3/fastq-scan)
  * reads a FASTQ and outputs summary statistics (read lengths, per-read qualities, per-base qualities)
  
Create conda environment.
```
% conda create --name microrunqc
% conda activate microrunqc
```
Install dependencies using [Conda](https://bioconda.github.io/user/install.html) and [Bioconda](https://bioconda.github.io/)
```
% conda install -c conda-forge -c bioconda -c defaults mlst skesa trimmomatic bwa fastq-scan
```

## Install and setup from source

```
% cd $HOME
% git clone https://github.com/estrain/MicroRunQC.git
% export PATH=$PATH:$HOME/MicroRunQC/bin
% chmod a+x $HOME/MicroRunQC/bin/*
% microrunqc.py --help
``` 
