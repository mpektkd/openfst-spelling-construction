#!/bin/bash

fstarcsort --sort_type=olabel ../fsts/M.binfst M_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/L.binfst L_sorted.binfst
fstcompose M_sorted.binfst L_sorted.binfst ML.binfst

fstarcsort --sort_type=olabel ML.binfst ML_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/N.binfst N_sorted.binfst
fstcompose ML_sorted.binfst N_sorted.binfst ../fsts/MLN.binfst

rm -r M_sorted.binfst L_sorted.binfst ML.binfst ML_sorted.binfst N_sorted.binfst

fstdraw ../fsts/MLN.binfst > MLN.dot
dot -Tpdf -oMLN.pdf MLN.dot

rm -r MLN.dot

