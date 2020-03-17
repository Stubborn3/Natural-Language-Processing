from sklearn.feature_extraction import stop_words
import re
from string import punctuation as punc
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
from nltk import ngrams
import itertools

   

class MovieAndTV:
    
    def __init__(self):
        self.domain,self.label,self.rating,self.review = [],[],[],[] 
        self.reviews = []
        self.unigrams, self.bigrams, self.trigrams = [],[],[]
        nltk.download('wordnet')
    
    def readData(self):
        data = open('Movies_TV.txt').read()
        data = re.sub('Domain.*\n','',data)
        dataInRows = data.split('\n')
        dataInRows.remove(dataInRows[-1])
        
        for column in dataInRows:
            d,l,rt,rv = column.split('\t')
            self.domain.append(d)
            self.label.append(l)
            self.rating.append(rt)
            self.review.append(rv)

    def removeWhiteSpaces(self):
        for i in range(len(self.review)):
            self.reviews.append(self.review[i].split(' '))
    #    print(self.reviews[999])

    
    def normalizeData(self):
        rev = self.reviews
        self.reviews = []
        for i in range(len(rev)):
            string  = ' '.join(rev[i]).lower()
            self.reviews.append(string.split(' '))
            #print(" ".join(self.reviews[9]))
        #print(self.reviews[0])

    def removingStopWords(self):
        stopWords = list(stop_words.ENGLISH_STOP_WORDS)
        reviewRSW = self.reviews
        self.reviews = []
        for i in range(len(reviewRSW)):
            rev = [] 
            for j in range(len(reviewRSW[i])):
                if reviewRSW[i][j] not in stopWords:
                    rev.append(reviewRSW[i][j])
            self.reviews.append(rev)
        #print(self.reviews[999])

    def removingPuntuations(self):
        reviewRP = self.reviews
        self.reviews = []
        for i in range(len(reviewRP)):
            sentence = ""
            string = ' '.join(reviewRP[i])
            for char in string:
                if char not in punc:
                    sentence += char
                else:
                    sentence += ' '
            self.reviews.append(sentence.split(' '))
            while("" in self.reviews[i]): 
                self.reviews[i].remove("")
    
    def stemmingWords(self):
        ps = PorterStemmer()
        reviewSW = self.reviews
        self.reviews = []
        for i in range(len(reviewSW)):
            rev = [] 
            for j in range(len(reviewSW[i])):
                rev.append(ps.stem(reviewSW[i][j]))
            self.reviews.append(rev)
        #print(self.reviews[0])

    def lemmatizingWords(self):
        wnl = WordNetLemmatizer()
        reviewLW = self.reviews
        self.reviews = []
        for i in range(len(reviewLW)):
            rev = [] 
            for j in range(len(reviewLW[i])):
                rev.append(wnl.lemmatize(reviewLW[i][j],'v'))
            self.reviews.append(rev)
        #print(self.review[0])    
        #print(self.reviews[0])
    
    def findNGrams(self):
        self.unigrams = list(ngrams(self.reviews[0],1))
        self.bigrams = list(ngrams(self.reviews[0],2))
        self.trigrams = list(ngrams(self.reviews[0],3))
        print("Unigrams: ",self.unigrams)
        print("Bigrams: ",self.bigrams)
        print("Trigrams: ",self.trigrams)
    
    def findProbabilityNGrams(self):
        #Reviews = list(itertools.chain(*self.reviews))
        probOfUniGrams = [self.unigrams.count(word)/len(set(self.unigrams)) for word in self.unigrams]
        print(probOfUniGrams)

        probOfBiGrams = [self.bigrams.count(words)/self.reviews[0].count(words[0]) for words in self.bigrams] 
        print(probOfBiGrams)
        
        probOfTriGrams = [self.trigrams.count(words)/self.bigrams.count(words[:2]) for words in self.trigrams]
        #print(self.trigrams)
        print(probOfTriGrams)
    
    def informationAboutReviews(self):
        tokens = 0
        rev = 0
        lst_review = []
        for i in range(len(self.reviews)):
            for j in self.reviews[i]:
                lst_review.append(j)
            rev += len(' '.join(self.reviews[i]))
            tokens += len(self.reviews[i])
        print("Total Tokens: ", tokens)

        wordNP = []
        for i in range(len(self.review)):
            words = self.review[i].split(' ')
            for p in words:
                wordNP.append(p)

        print("Total Unique Tokens Before preprocessing: ", len(set(wordNP)))
        print("Total Unique Tokens After preprocessing: ", len(set(lst_review)))
        print("Average Length of a review: ", rev/len(self.reviews))
        print("Average Length of tokens in a review: ", tokens/len(self.reviews))
        

obj = MovieAndTV()
obj.readData()
obj.removeWhiteSpaces()
obj.normalizeData()
obj.removingStopWords()
obj.removingPuntuations()
obj.stemmingWords()
obj.lemmatizingWords()
obj.findNGrams()
obj.findProbabilityNGrams()
obj.informationAboutReviews()