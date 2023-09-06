#!/usr/bin/python

import sys 
import subprocess
# function that return key from a value in a dictionary
def GetKey(val):
   for key, value in dict.items():
      if val == value:
         return key

#create dictionary that has as key the expected word and as values all the mispelled
dict = {}
with open("../data/spell_test.txt", "r") as file:
    for line in file:
        k, v = line.split(":",-1)
        k = k.strip("\t")
        v = v.strip("\n")
        v = v.split(" ",-1)
        while("" in v) :
            v.remove("") 
        dict[k] = v 

#print(dict)
set_of_words = list(dict.values())  #break in sets with same key
#get the corrected word via ./predict and store it in predict_output.txt
for sow in set_of_words:
    key = GetKey(sow)
    for word in sow:
        corrected = subprocess.getoutput('./predict.sh ../fsts/S.binfst {}'.format(word))
        with open("../data/predict_output_S.txt","a") as f:
            f.write("{} : {} -> {}\n".format(key, word, corrected))
