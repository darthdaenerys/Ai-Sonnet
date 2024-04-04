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