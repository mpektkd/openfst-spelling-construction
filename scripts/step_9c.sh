#!/bin/bash

fstarcsort --sort_type=olabel ../fsts/L.binfst L_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V.binfst V_sorted.binfst
fstcompose L_sorted.binfst V_sorted.binfst LV.binfst

fstarcsort --sort_type=olabel LV.binfst LV_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/W.binfst W_sorted.binfst
fstcompose LV_sorted.binfst W_sorted.binfst ../fsts/LVW.binfst

rm -r L_sorted.binfst V_sorted.binfst LV.binfst LV_sorted.binfst W_sorted.binfst


