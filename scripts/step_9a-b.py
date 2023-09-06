#!/usr/bin/python

import sys 
import math

#create dictionary that has as key the word and as values the # of appearance
dict = {}
with open("../vocab/words.vocab.txt", "r") as file:
    for line in file:
        k, v = line.split("\t ",-1)
        v = v.strip("\n")
        dict[k] = v 

F = 0
for v in dict.values():
    F += int(v)  #calculate the sum of values

with open('../fsts/W.fst', 'w') as file:
    for k in dict.keys(): #constract all:all/freq
        file.write("0\t 0\t {}\t {}\t {}\n".format(k, k, round((-1)*math.log(float(dict[k])/F),3)))
    # Final state
    file.write('0')
