# MicroRunQC
Generate Metrics and Summary Statistics for Bacterial WGS

## Dependencies 

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
  
Install dependencies using [Conda](https://bioconda.github.io/user/install.html) and [Bioconda](https://bioconda.github.io/)
```
% conda install -c conda-forge -c bioconda -c defaults mlst skesa trimmomatic bwa fastq-scan
```

## Install from source

```
% cd $HOME
% git clone https://github.com/estrain/MicroRunQC.git
% $HOME/MicroRunQC/bin/microrunqc.py --help
``` 
