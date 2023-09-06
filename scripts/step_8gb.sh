#!/bin/bash

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/cit.fst cit.binfst
fstdraw cit.binfst > cit.dot
dot -Tpdf -ocit.pdf cit.dot
rm -r cit.binfst cit.dot

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/cit.fst | fstcompose - ../fsts/EV.binfst | fstshortestpath > shortest_cit.binfst
fstdraw shortest_cit.binfst > shortest_cit.dot
dot -Tpdf -oshortest_cit_EV.pdf shortest_cit.dot
rm -r shortest_cit.binfst shortest_cit.dot

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/cwt.fst cwt.binfst
fstdraw cwt.binfst > cwt.dot
dot -Tpdf -ocwt.pdf cwt.dot
rm -r cwt.binfst cwt.dot

fstcompile --isymbols=../vocab/chars.syms --osymbols=../vocab/chars.syms --keep_isymbols --keep_osymbols ../fsts/cwt.fst | fstcompose - ../fsts/EV.binfst | fstshortestpath > shortest_cwt.binfst 
fstdraw shortest_cwt.binfst > shortest_cwt.dot
dot -Tpdf -oshortest_cwt_EV.pdf shortest_cwt.dot
rm -r shortest_cwt.binfst shortest_cwt.dot
