#!/bin/bash

fstarcsort --sort_type=olabel ../fsts/E.binfst E_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V.binfst V_sorted.binfst
fstcompose E_sorted.binfst V_sorted.binfst ../fsts/EV.binfst

rm -r E_sorted.binfst V_sorted.binfst
