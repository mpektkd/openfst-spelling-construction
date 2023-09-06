import logging
import multiprocessing
import os
from w2v_train import W2VLossLogger
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from string import Template
from gensim.models import KeyedVectors
from shutil import copy
import glob

SCRIPT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
models_dir = os.path.join(SCRIPT_DIRECTORY, "../data/gutenberg_models")
samples = glob.iglob(os.path.join(models_dir, "*.model"))
temp1 = Template("$i)The prediction of $sample for $task\n")
#open an output file to store the statistcs
with open('predict.txt', 'w') as file:
    temp = Template('Word: $a, Most Similar: $s, Cosine Distance: $c\n')
    i = 1
    for sample in samples:
        model = Word2Vec.load(sample)  #load our model
        if sample == os.path.join(models_dir,"gutenberg_with_20_min_w2v.100d.model"):
            file.write(temp1.substitute(i = str(i),sample = os.path.basename(sample), task = "(12c)"))
            print(temp1.substitute(i = str(i),sample = os.path.basename(sample), task = "(12c)"))
            predictions = {}            
            for word in ['book','bank','water']:
                predictions[word] = model.wv.most_similar(word, topn=1)     #call function to find the most similar according to cosine distance
                file.write(temp.substitute(a = word, s = predictions[word][0][0], c = predictions[word][0][1]))
                print("Word: %a, Most Similar: %s, Cosine Distance: %s"  %(word, predictions[word][0][0], predictions[word][0][1]))
            file.write('\n')
            i +=1
        else:
            file.write(temp1.substitute(i = str(i),sample = os.path.basename(sample), task = "(12c)"))
            print(temp1.substitute(i = str(i), sample = os.path.basename(sample), task = "(12c)"))
            predictions = {}            
            for word in ['bible','book','bank','water']:
                predictions[word] = model.wv.most_similar(word, topn=1)     #call function to find the most similar according to cosine distance
                file.write(temp.substitute(a = word, s = predictions[word][0][0], c = predictions[word][0][1]))
                print("Word: %a, Most Similar: %s, Cosine Distance: %s"  %(word, predictions[word][0][0], predictions[word][0][1]))
            file.write('\n')
            i +=1
        

copy('predict.txt', '../data')
os.remove('predict.txt')

        