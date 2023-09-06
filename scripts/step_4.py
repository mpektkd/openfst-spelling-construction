#!/usr/bin/python 

alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet = "ab"
weight = {
        "delete": 1,
        "insert": 1,
        "sub": 1
        }

with open('../fsts/L.fst', 'w') as file:
    # No edit
    for l in alphabet:
        file.write("0\t 0\t {}\t {}\t 0\n".format(l, l))

    # Deletes: input character, output epsilon
    for l in alphabet:
        file.write("0\t 0\t {}\t ε\t {}\n".format(l,weight["delete"]))
        
    # Insertions: input epsilon, output character
    for l in alphabet:
        file.write("0\t 0\t ε\t {}\t {}\n".format(l,weight["insert"]))

    # Substitutions: input one character, output another
    for l in alphabet:
        for r in alphabet:
            if l is not r:
                file.write("0\t 0\t {}\t {}\t {}\n".format(l, r,weight["sub"]))
                        
    # Final state
    file.write('0')
