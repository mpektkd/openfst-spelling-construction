#!/bin/bash

fstdraw ../fsts/W.binfst > W.dot
dot -Tpdf -oW.pdf W.dot
rm -r W.dot

fstarcsort --sort_type=olabel ../fsts/V.binfst V_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/W.binfst W_sorted.binfst
fstcompose V_sorted.binfst W_sorted.binfst VW.binfst
fstdraw VW.binfst > VW.dot
dot -Tpdf -oVW.pdf VW.dot
rm -r V_sorted.binfst W_sorted.binfst VW.binfst VW.dot
