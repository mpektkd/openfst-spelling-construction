#!/bin/bash

fstcompile --isymbols=chars.syms --osymbols=words_en_50k.syms --keep_isymbols --keep_osymbols Union.fst Union.binfst
fstrmepsilon Union.binfst | fstdeterminize | fstminimize >../fsts/V_en_50k.binfst 
fstprint ../fsts/V_en_50k.binfst >../fsts/V_en_50k.fst

rm Union.fst words_en_50k.syms chars.syms Union.binfst


fstcompile --isymbols=../vocab/words_en_50k.syms --osymbols=../vocab/words_en_50k.syms --keep_isymbols --keep_osymbols ../fsts/W_en_50k.fst ../fsts/W_en_50k.binfst

fstarcsort --sort_type=olabel ../fsts/E_smoothing.binfst E_smoothing_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/V_en_50k.binfst V_en_50k_sorted.binfst
fstcompose E_smoothing_sorted.binfst V_en_50k_sorted.binfst EV_smoothing_en_50k.binfst

fstarcsort --sort_type=olabel EV_smoothing_en_50k.binfst EV_smoothing_en_50k_sorted.binfst
fstarcsort --sort_type=ilabel ../fsts/W_en_50k.binfst W_en_50k_sorted.binfst
fstcompose EV_smoothing_en_50k_sorted.binfst W_en_50k_sorted.binfst ../fsts/EVW_smoothing_en_50k.binfst

rm -r E_smoothing_sorted.binfst V_en_50k_sorted.binfst EV_smoothing_en_50k.binfst EV_smoothing_en_50k_sorted.binfst W_en_50k_sorted.binfst




