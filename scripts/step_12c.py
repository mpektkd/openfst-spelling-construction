import logging
import multiprocessing
import os
from w2v_train import W2VLossLogger
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from string import Template
from gensim.models import KeyedVectors
from shutil import copy

#open an output file to store the statistcs
with open('predictions.txt', 'w') as file:
    
    temp = Template('Word: $a, Most Similar: $s, Cosine Distance: $c\n')

    model = Word2Vec.load("../data/gutenberg_w2v.100d.model")  #load our model

    file.write("The predictions of our model for (12c)\n")    
    print("The predictions of our model for (12c)")
    predictions = {}
    for word in ['bible','book','bank','water']:
        predictions[word] = model.wv.most_similar(word, topn=1)     #call function to find the most similar according to cosine distance
        file.write(temp.substitute(a = word, s = predictions[word][0][0], c = predictions[word][0][1]))
        print("Word: %a, Most Similar: %s, Cosine Distance: %s"  %(word, predictions[word][0][0], predictions[word][0][1]))

    file.write("The predictions of our model for (12d)\n")
    print("The predictions of our model for (12d)")
    pred = {}
    for word in [('girls', 'queen', 'kings'),('good', 'tall', 'taller'),('france', 'paris', 'london')]:
        pred[word] = model.wv.most_similar(positive=[word[0], word[2]], negative=[word[1]], topn=1)
        file.write(temp.substitute(a = word, s = pred[word][0][0], c = pred[word][0][1]))
        print("Word: %s, Most Similar: %s, Cosine Distance: %s"  %(word, pred[word][0][0], pred[word][0][1]))


    g_model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True,limit=10000000)       #load google news keyedvectors

    file.write("The predictions of google's model for (12c)\n")
    print("The predictions of google's model for (12c)")
    pred = {}
    for word in [('girls', 'queen', 'kings'),('good', 'tall', 'taller'),('france', 'paris', 'london')]:
        pred[word] = g_model.wv.most_similar(positive=[word[0], word[2]], negative=[word[1]], topn=1)
        file.write(temp.substitute(a = word, s = pred[word][0][0], c = pred[word][0][1]))
        print("Word: %s, Most Similar: %s, Cosine Distance: %s"  %(word, pred[word][0][0], pred[word][0][1]))

    file.write("The predictions of google's model for (12d)\n")
    print("The predictions of google's model for (12d)")
    pred = {}
    for word in ['bible','book','bank', 'water']:
        pred[word] = g_model.wv.most_similar(word, topn=1)
        file.write(temp.substitute(a = word, s = pred[word][0][0], c = pred[word][0][1]))
        print("Word: %s, Most Similar: %s, Cosine Distance: %s"  %(word, pred[word][0][0], pred[word][0][1]))

copy('predictions.txt', '../data')      #transfer predictions.txt to data dir
os.remove('predictions.txt')