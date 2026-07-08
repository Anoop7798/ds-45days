import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
text="i love machine learning"
#tokens = word_tokenize(text)
#print(tokens)

text1="Anoop gurjar from Haryana"

tokens = word_tokenize(text1)
print(tokens)

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text= "i am learning machine learning "
words=word_tokenize(text)
print("rokenize")
print(words)

stopwords=set(stopwords.words("english"))
print("stop words")
print(stopwords)

#filter data
filtered=[]

for word in words:
    if word.lower() not in stopwords:
        filtered.append(word)
        
        
#print filter data
print("filter data")
print(filtered)



#stemming ->  converts words into their root form
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
print(stemmer.stem("playing"))
print(stemmer.stem("played"))
print(stemmer.stem("player"))

print(stemmer.stem("running"))
print(stemmer. Stem("runner"))

#create a project with combination of above all
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Input text
text = "I am learning Machine Learning and playing cricket."

# Tokenization
words = word_tokenize(text)
print("Tokens:")
print(words)

# Stopword Removal
stop_words = set(stopwords.words("english"))

filtered = []
for word in words:
    if word.lower() not in stop_words:
        filtered.append(word)

print("\nAfter Removing Stopwords:")
print(filtered)

# Stemming
stemmer = PorterStemmer()

print("\nStemmed Words:")
for word in filtered:
    print(word, "->", stemmer.stem(word))
    
    
     
#create a project with combinatiion of word_tokenize ,stopword and porterStemmer
 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
 
 
text= input("Enter a sentence: ")
 
#tokenization
tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)
 
# \remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]
 
#remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in tokens if word.lower() not in stop_words]
 
print("\nAfter Removing Stopwords:")
print(filtered_words)
 
#stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]
 
print("\nStemmed Words:")
print(stemmed_words)
 
