import nltk
import random
from nltk.corpus import movie_reviews
import pickle
import indiv # written by me
from nltk.corpus import PlaintextCorpusReader

def find_features(document):
	# when convert list -> set get one iteration of unique element
	words = set(document)
	features = {} # dictionary
	for x in word_features:
		features[x] = (x in words) # boolean value
	return features


dir1 = "blurbs/pos"
dir2 = "blurbs/neg"

moviedata = [(list(movie_reviews.words(fileid)), category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]


temp = indiv.prepData(dir1)
posData = indiv.mostCommonWords(temp)
temp = indiv.prepData(dir2)
negData = indiv.mostCommonWords(temp)
runData = posData + negData


random.shuffle(moviedata)
random.shuffle(runData)


# find most common and neg/pos
all_words = []
for x in movie_reviews.words():
	all_words.append(x.lower())
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000] # use top 3000 words 


# NEXT SEE IF FEATURE WORDS APPEAR IN TXT

# convert words to features (contained in each review)
featuresets = [(find_features(rev), category) for (rev, category) in moviedata]
myfeatures = [(find_features(rev), category) for (rev, category) in runData]


training_set = featuresets[:1900]
testing_set = myfeatures[:1900]



# USE PICKLED THE CLASSIFIER 

# classifier = nltk.NaiveBayesClassifier.train(training_set)
# rb = read byte
classifier_f = open("niavebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Accuracy", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features()


# USED TO PICKLE THE CLASSIFIER (ONLY NEEDS TO BE DONE ONCE)
# UNCOMMENT AND RUN IF NEED TO UPDATE .PICKLE

# save_classifier = open("niavebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

