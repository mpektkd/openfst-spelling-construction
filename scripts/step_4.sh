#!/bin/bash

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/L.fst ../fsts/L.binfst
#fstdraw ../fsts/L.binfst > L.dot
#dot -Tpdf -oL.pdf L.dot


