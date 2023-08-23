
import unicodedata
import re

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd




# Creating a function to clean string
def basic_clean(string):

    clean_str = string.lower()
    clean_str = unicodedata.normalize('NFKD', clean_str)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    clean_str = re.sub(r"[^a-z0-9'\s]", '', clean_str)

    return clean_str







def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # make our tokenizer, taken from nltk's ToktokTokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # apply our tokenizer's tokenization to the string being input, ensure it returns a string
    string = tokenizer.tokenize(string, return_str = True)
    
    return string







def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # assign our stopwords from nltk into stopword_list
    stopword_list = stopwords.words('english')
    # utilizing set casting, i will remove any excluded stopwords
    stopword_set = set(stopword_list) - set(exclude_words)
    # add in any extra words to my stopwords set using a union
    stopword_set = stopword_set.union(set(extra_words))
    # split our document by spaces
    words = string.split()
    # every word in our document, as long as that word is not in our stopwords
    filtered_words = [word for word in words if word not in stopword_set]
    # glue it back together with spaces, as it was so it shall be
    string_without_stopwords = ' '.join(filtered_words)
    # return the document back
    return string_without_stopwords







def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # create our stemming object
    ps = nltk.porter.PorterStemmer()
    # use a list comprehension => stem each word for each word inside of the entire document,
    # split by the default, which are single spaces
    stems = [ps.stem(word) for word in string.split()]
    # glue it back together with spaces, as it was before
    string = ' '.join(stems)
    
    return string






def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # create our lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    # use a list comprehension to lemmatize each word
    # string.split() => output a list of every token inside of the document
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    # glue the lemmas back together by the strings we split on
    string = ' '.join(lemmas)
    #return the altered document
    return string