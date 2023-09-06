#!/usr/bin/python

import sys 
import subprocess

with open('../data/wiki.txt') as f:     #open file
    for line in f:  #read all lines
        m, n = line.split("\t",-1)  #split 2 words in each line
        n = n.strip("\n")
        change = subprocess.getoutput('./word_edits.sh {} {}'.format(m, n)) #call word_edits and store output
        with open("../data/word_edits_output.txt","a") as q:                #into file word_edits_output.txt
            q.write("{}\n".format(change))
             
