#!/bin/bash

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/E.fst ../fsts/E.binfst
#fstdraw ../fsts/E.binfst > E.dot
#dot -Tpdf -oE.pdf E.dot
