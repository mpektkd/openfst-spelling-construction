#!/usr/bin/python

import re
import sys
import math

rr = 0 #test to see if we assign correct frequencies

# fuction that returns the weight for each arc based on the frequency we calculated
def weight(source,target,dictionary):
    global rr   #test
    for k in dictionary.keys():
        if ((source == k[0]) and (target == k[1])):     # k = (s,t) so k[0]=s and k[1]=t
            rr += dictionary[k]/F_smoothing #test
            return round((-1)*math.log(float(dictionary[k])/F_smoothing),3) #cost
    rr += 1/F_smoothing #test
    return round((-1)*math.log(1/F_smoothing),3) # ADD-1 SMOOTHING cost


dictionary = {} #create dectiorary (source,target): # of appearance
with open('../data/word_edits_output.txt') as f:     #open file with edits
    for line in f:  #read all lines
        s, t = line.split("\t",-1)  #split the chars (s,t) in each line
        t = t.strip("\n")
        key = (s,t)    # create tuple with key
        if key not in dictionary.keys():
            dictionary[key] = 1     #first appearance, initialize with value 1 (ADD-1 SMOOTHING)
        dictionary[key] += 1    #value += 1 for every copy

F = 0
num_of_edits = 0
for v in dictionary.values():
    F += v  #calculate the sum of values
    num_of_edits += 1 #calculate number of edits in dictionary 

F_smoothing = F + 27*26 -num_of_edits #the divisor to calculate frequency | 27*26 == # of possible edits without {x:x} edits

alphabet = "abcdefghijklmnopqrstuvwxyz"

with open('../fsts/E_smoothing.fst', 'w') as file:
    # No edit
    for l in alphabet:
        file.write("0\t 0\t {}\t {}\t 0\n".format(l, l))

    # Deletes: input character, output epsilon
    for l in alphabet:
        file.write("0\t 0\t {}\t ε\t {}\n".format(l,weight(l,'ε',dictionary)))

    # Insertions: input epsilon, output character
    for l in alphabet:
        file.write("0\t 0\t ε\t {}\t {}\n".format(l,weight('ε',l,dictionary)))

    # Substitutions: input one character, output another
    for l in alphabet:
        for r in alphabet:
            if l is not r:
                file.write("0\t 0\t {}\t {}\t {}\n".format(l, r,weight(l,r,dictionary)))

    # Final state
    file.write('0')

#print(rr) #test
