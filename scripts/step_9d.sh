#!/bin/bash

fstarcsort --sort_type=olabel ../fsts/E.binfst E_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V.binfst V_sorted.binfst
fstcompose E_sorted.binfst V_sorted.binfst EV.binfst

fstarcsort --sort_type=olabel EV.binfst EV_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/W.binfst W_sorted.binfst
fstcompose EV_sorted.binfst W_sorted.binfst ../fsts/EVW.binfst

rm -r E_sorted.binfst V_sorted.binfst EV.binfst EV_sorted.binfst W_sorted.binfst



