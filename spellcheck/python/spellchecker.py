import re
import os
from os import listdir
from os.path import isfile, join
from collections import Counter
import numpy

def words(text): return re.findall(r'\w+', text.lower())

#WORDS = Counter(words(open('coba.rtf').read()))

def load_book(path):
    input_file = os.path.join(path)
    with open(input_file) as f:
        book = f.read()
    return book

path = 'spellcheck/python/books/';
book_files = [f for f in listdir(path) if isfile(join(path, f))]
book_files = book_files[1:]

books = []
for book in book_files:
    books.append(load_book(path+book))
print(len(books))
for i in range(len(books)):
    print("There are {} words in {}.".format(len(books[i].split()), book_files[i]))

books[0][:500]

def clean_text(text):
    '''Remove unwanted characters and extra spaces from the text'''
    text = re.sub(r'\n', ' ', text) 
    text = re.sub(r'[{}@_*>()\\#%+=\[\]]','', text)
    text = re.sub('a0','', text)
    text = re.sub('\'92t','\'t', text)
    text = re.sub('\'92s','\'s', text)
    text = re.sub('\'92m','\'m', text)
    text = re.sub('\'92ll','\'ll', text)
    text = re.sub('\'91','', text)
    text = re.sub('\'92','', text)
    text = re.sub('\'93','', text)
    text = re.sub('\'94','', text)
    text = re.sub('\.','. ', text)
    text = re.sub('\!','! ', text)
    text = re.sub('\?','? ', text)
    text = re.sub(' +',' ', text)
    return text

clean_books = []
for book in books:
    clean_books.append(clean_text(book))

clean_books[0][:500]

vocab_to_int = {}
count = 0
for book in clean_books:
    for character in book:
        if character not in vocab_to_int:
            vocab_to_int[character] = count
            count += 1

sentences = []
for book in clean_books:
    for sentence in book.split('. '):
        sentences.append(sentence + '.')
print("There are {} sentences.".format(len(sentences)))

Tokens = []
for each_line in sentences:
    each_line = re.sub('[.]','', each_line)
    token = each_line.split()

    for each_word in token:
    	Tokens.append(each_word)

WORDS = Counter(Tokens)

def P(word, N=sum(WORDS.values())): 
     # "Probability of `word`."
     return WORDS[word] / N

def correction(word):
    # "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    # "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    # "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    # "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
    deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
    inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    # "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# while True:
#     kata = input("input kata : ")
#     print('kata typo : ', kata)
#     if kata == 'exit':
#         break
#     else:
#         print('koreksi : ', candidates(kata))

def testSpellCheck(word):
    return candidates(word)