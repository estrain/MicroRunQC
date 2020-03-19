# MicroRunQC
Generate Metrics and Summary Statistics for Bacterial WGS

## Dependencies 

* [SKESA](https://github.com/ncbi/SKESA)
  * Strategic k-mer extension for scrupulous assemblies
* [mlst](https://github.com/tseemann/mlst)
  * Scan contig files against traditional PubMLST typing schemes
* [trimmomatic](https://github.com/timflutre/trimmomatic)
  * A flexible read trimming tool for Illumina NGS data
  
Install dependencies using [Conda](https://bioconda.github.io/user/install.html) and [Bioconda](https://bioconda.github.io/)
```
% conda install -c conda-forge -c bioconda -c defaults mlst skesa trimmomatic
```

## Install from source

```
% cd $HOME
% git clone https://github.com/estrain/MicroRunQC.git
% $HOME/MicroRunQC/bin/microrunqc.py --help
``` 
