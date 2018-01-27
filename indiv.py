from __future__ import division 
import nltk, re, pprint, codecs
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import state_union
from collections import Counter
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import ngrams
from nltk import pos_tag

english_stopwords = stopwords.words('english')


def prepData(setdir):
	cor = []
	senti = setdir[-3:]
	files = ".*.txt"
	corpustemp = PlaintextCorpusReader(setdir, files)
	corpus  = nltk.Text(corpustemp.words())
	corpus = [x.lower() for x in corpus] # eliminate counting same word twice due to case sensitivity

	# stemming -> take root stem of words
	stemmer = PorterStemmer()
	stemmed_corpus = []
	for x in corpus:
		stemmed_corpus_elm = x
		stemmed_corpus.append((stemmed_corpus_elm, senti))

	return stemmed_corpus


def mostCommonWords(corpus):
	all_common = []
	# Counter -> Given a list count the amount of unique elements in the list
	frequencies = Counter(corpus)
	for token, count in frequencies.most_common(3000):

		# if a stopword is found don't count it || if one char long
		if token in english_stopwords or len(token) < 2:
			continue
		all_common.append((token))
	return all_common


def getBigrams(corpus):
	all_bigrams = []	
	for x in corpus:
		bigrams = list(ngrams(corpus,2))
		all_bigrams = all_bigrams + bigrams

	frequencies = Counter(all_bigrams)
	for token, count in frequencies.most_common(250):
		print token, count


# tag each word in sentence 
# -> https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
def tagSent(corpus): 
	tags = pos_tag(corpus)
	# for this to work need to comment out corpus.lower() -> Capitalization on names
	namedEnt = nltk.ne_chunk(tags, binary = True)
	namedEnt.draw()



