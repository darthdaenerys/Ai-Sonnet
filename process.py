import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
import numpy as np
import random
import json
import re
import pickle


with open('hyperparameters.json','r') as f:
    params=json.load(f)
with open('models/vocabulary.h5','rb') as f:
    id2word=pickle.load(f)
    word2id=pickle.load(f)

sonnet_model=load_model('models/sonnet_model.h5',compile=False)
max_sequence_length=params['max_sequence_length']
max_tokens=params['max_tokens']

def sequences2ids(sequence):
    ids=[]
    sequence=re.sub('\n',' <NEXT> ',sequence.lower())
    sequence=re.sub('.',' . ',sequence)
    sequence=re.sub(',',' , ',sequence)

    for word in sequence.split():
        ids.append(word2id[word])
    return ids

def ids2sequences(ids):
    decode=[]
    if type(ids)==int:
        ids=[ids]
    for id in ids:
        decode.append(id2word[id])
    decode=' '.join(decode)
    decode=re.sub(' <NEXT> ',' \n ',decode)
    decode=re.sub(' , ',', ',decode)
    decode=re.sub(' . ','. ',decode)
    return decode