#!/bin/bash

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/M.fst ../fsts/M.binfst
fstdraw ../fsts/M.binfst > M.dot
dot -Tpdf -oM.pdf M.dot

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/N.fst ../fsts/N.binfst
fstdraw ../fsts/N.binfst > N.dot
dot -Tpdf -oN.pdf N.dot

rm -r M.dot N.dot

