#!/usr/bin/python

# *** ERVTHMA A*** #
character = [chr(i) for i in range(ord('a'), ord('z') + 1)] #create list with all lowercase letters 
#print(character) #print for check

ascii_dic = {} #dictionary for letters and ascii codes
ascii_dic['ε'] = 0  #add <eps> in dic
for ch in character:
    ascii_dic[ch] = ord(ch) #add lowercase letter to dic

#print(ascii_dic) #print for check

with open('../vocab/chars.syms','w') as file:  #print dic to output file
    for k, v in ascii_dic.items():
        file.write("{}\t {}\n".format(k, v))

# *** ERVTHMA B*** #
dic_1 = {}  #load dictionary from step_2
with open(r"../vocab/words.vocab.txt", "r") as f:
    for line in f:
        k, v = line.split(" ",1)
        k = k.strip("\t")
        v = int(v.strip("\n"))
        dic_1[k] = v
                                    
#print(dic_1) #print for check

dic_2 = {} #new dictionary with diffrent number (starting from 0) for each word
dic_2['ε'] = 0  #add <eps> in dic
i = 1   #save 0 position to add <eps> 
for word in dic_1.keys():
    dic_2[word] = i
    i += 1

#print(dic_2) #print for check

with open('../vocab/words.syms','w') as file:    #save new dictionary in 'words.syms'
    for k, v in dic_2.items():
        file.write("{}\t {}\n".format(k, v))
