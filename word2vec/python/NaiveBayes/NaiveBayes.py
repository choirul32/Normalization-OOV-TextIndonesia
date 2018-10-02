import csv
import random
import nltk
from nltk.util import ngrams
#from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from normalization.python.word2vec_NormalizationTrain import testNormalization

#factory = StemmerFactory()
#stemmer = factory.create_stemmer()

def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

filename = 'word2vec/python/naivebayes/corpus.csv'
dataset = loadCsv(filename)
splitRatio = 0.70
training_set, testing_set = splitDataset(dataset, splitRatio)

def word_features(word):
    return dict(((ng, True) for ng in ngrams(word.lower(),4)))

training_set = [(word_features(n), jenis_kata) for (n, jenis_kata) in training_set]
testing_set = [(word_features(n), jenis_kata) for (n, jenis_kata) in testing_set]
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent: ",nltk.classify.accuracy(classifier, testing_set)*100)
classifier.show_most_informative_features()


def testClassification(text):
	#text = stemmer.stem(text)
	if classifier.classify(word_features(text))=='Baku':
		return "Kata Baku"
	else:
		hasil = testNormalization(text)
		return hasil


