#!/bin/bash

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/E_smoothing.fst ../fsts/E_smoothing.binfst

fstarcsort --sort_type=olabel ../fsts/E_smoothing.binfst E_smoothing_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V.binfst V_sorted.binfst
fstcompose E_smoothing_sorted.binfst V_sorted.binfst ../fsts/EV_smoothing.binfst

rm -r E_smoothing_sorted.binfst V_sorted.binfst

