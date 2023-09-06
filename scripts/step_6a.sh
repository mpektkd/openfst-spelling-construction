#!/bin/bash

fstarcsort --sort_type=olabel ../fsts/L.binfst L_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V.binfst V_sorted.binfst
fstcompose L_sorted.binfst V_sorted.binfst ../fsts/S.binfst

rm -r L_sorted.binfst V_sorted.binfst

#fstdraw ../fsts/S.binfst > S.dot
#dot -Tpdf -oS.pdf S.dot
