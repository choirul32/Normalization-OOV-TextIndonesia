from gensim import utils
from gensim.models import Word2Vec
from gensim.models import TranslationMatrix
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile

import os
import codecs
import pandas as pd
import numpy as np

#get corpus translation pairs
print('Loading file dan Models...')
train_file = 'normalization/python/OPUS_source_target.txt'
with utils.smart_open(train_file, 'r') as f:
    pairs = [tuple(utils.to_unicode(line).strip().split()) for line in f]

#get word2vec model wiki
source_word_vec_file = 'normalization/python/models/Model_OutOfVocabulary/size100_mincount20_window5_iter10.model'
model_source = Word2Vec.load(source_word_vec_file)
model_source = model_source.wv

#get word2vec model OOV from self training
target_word_vec_file = 'normalization/python/models/Model_from_Wiki/model_100/idwiki_word2vec_100.model'
model_target = Word2Vec.load(target_word_vec_file)
model_target = model_target.wv

pairs = list(pairs)
('Removing Missing Vocabulary in List')
print('length list before pairs : '+str(len(pairs)))

list_pairs = []

for n in range (len(pairs)-1):
    if pairs[n][0] in model_source.wv.vocab and pairs[n][1] in model_target.wv.vocab:
        list_pairs.append((pairs[n][0], pairs[n][1]))
        
print(len(pairs)-len(list_pairs))

pairs = list_pairs
pairs = tuple(pairs)
transmat = TranslationMatrix(model_source, model_target, pairs)
transmat.train(pairs)

def testNormalization(word):
	try:
		translate = transmat.translate([word], topn=3, source_lang_vec=model_source, target_lang_vec=model_target)
		return translate[word]
	except:
		return "tidak ditemukan"
    	
