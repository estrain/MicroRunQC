# MicroRunQC
Generate Metrics and Summary Statistics for Bacterial WGS

## Dependencies 
Install dependencies using [Conda](https://bioconda.github.io/user/install.html) and [Bioconda](https://bioconda.github.io/)
```
% conda install -c conda-forge -c bioconda -c defaults mlst skesa trimmomatic
```
* [SKESA](https://github.com/ncbi/SKESA)
* [mlst](https://github.com/tseemann/mlst)
* [trimmomatic](https://github.com/timflutre/trimmomatic)

## Install from source

```
% cd $HOME
% git clone https://github.com/estrain/MicroRunQC.git
% $HOME/MicroRunQC/bin/microrunqc.py --help
``` 
