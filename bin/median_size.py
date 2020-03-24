#!/usr/bin/env python

## Errol Strain (estrain@gmail.com)
## calculate median insert size from sam file

import numpy as np

def get_data(infile):
    lengths = []
    for line in infile:
        if line.startswith('@'):
            pass
        else:
            line = line.rsplit()
            length = int(line[8])
            if length > 0:
                lengths.append(length)
            else:
                pass
    return lengths

if __name__ == "__main__":
    import sys
    lengths = get_data(sys.stdin)
    md = int(np.median(lengths))
print(md, end = '')
