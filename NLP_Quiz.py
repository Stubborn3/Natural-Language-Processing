from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re

class MovieAndTV:

    def __init__(self):
        self.review = []

    def readData(self):
        data = open('Movies_TV.txt').read()
        data = re.sub('Domain.*\n','',data)
        dataInRows = data.split('\n')
        dataInRows.remove(dataInRows[-1])
        
        for column in dataInRows:
            _,_,_,rv = column.split('\t')
            self.review.append(rv)
    
    def structureRepresentation(self):
        
        print("Structure with Binary")
        vecBinary = CountVectorizer(ngram_range = (1,3),min_df = 10,max_df = 100, max_features = 1000, binary = True)
        data = vecBinary.fit_transform(self.review)
        print(data)

        print("Structure with Frequency")
        vecFreq = CountVectorizer(ngram_range = (1,3),min_df = 10,max_df = 100, max_features = 1000)
        data = vecFreq.fit_transform(self.review)
        print(data)

        print("Structure with TFidF")
        vecTfid = TfidfVectorizer(ngram_range = (1,3),min_df = 10,max_df = 100, max_features = 1000)
        data = vecTfid.fit_transform(self.review)
        print(data)

        features = vecTfid.get_feature_names()
        print(features[:20])

obj = MovieAndTV()
obj.readData()
obj.structureRepresentation()