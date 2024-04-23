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

def softmax(z):
    return np.exp(z)/sum(np.exp(z))

def sample(conditional_probability,temperature=1.0):
    conditional_probability = np.asarray(conditional_probability).astype("float64")
    conditional_probability = np.log(conditional_probability) / temperature
    reweighted_conditional_probability = softmax(conditional_probability)
    probas = np.random.multinomial(1, reweighted_conditional_probability, 1)
    return np.argmax(probas)

def generate_sequence(initial_seed,steps,temperature=1.0):
    gen=0
    encoded_seq=None
    if initial_seed=='':
        idx=random.randint(0,max_tokens-1)
        initial_seed=ids2sequences(idx)
    print(initial_seed,end='',flush=True)
    encoded_seq=sequences2ids(initial_seed)
    
    
    while gen!=steps:
        gen+=1
        input_seq=np.zeros((1,max_sequence_length))
        last_sequence=encoded_seq[len(encoded_seq)-max_sequence_length:]
        
        for idx,enc in enumerate(last_sequence):
            input_seq[:,idx]=enc
