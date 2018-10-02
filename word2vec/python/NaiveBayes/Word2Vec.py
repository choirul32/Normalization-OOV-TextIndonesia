from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import numpy as np
import os


def training(dataset):
	model = Word2Vec(dataset, size=100, sg = 0, min_count = 1, window = 5, iter = 10)
	return model

def saveModels(model):
	model.save('./modelWord2Vec.model')

def loadModels():
	new_model = Word2Vec.load('idwiki_word2vec_200/idwiki_word2vec_200.model')
	return new_model

def openTextSave(name):
	file = open(name, encoding="utf-8")
	sentences = []
	for line in file.read().splitlines():
		words = line.split()
		sentences.append(words)
	return sentences

def builtPlot(model):
	X = model[model.wv.vocab]
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)
	# create a scatter plot of the projection
	pyplot.scatter(result[:, 0], result[:, 1])
	words = list(model.wv.vocab)
	for i, word in enumerate(words):
		pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()

def summarizeWord(model):
	words = list(model.wv.vocab)
	print(words)

model = loadModels()#openTextSave("./save/sentences_twitter.txt")
#model = training(sentences_)
#saveModels(model)
#print(model.wv.most_similar(positive='jokowi'))
while True:
	input_ = input("masukan text : ")
	print(model.wv.most_similar(positive=input_))


