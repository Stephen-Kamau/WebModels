import pickle
import re


 # special chars
def special_char_removal(text):
    pattern=r'[^a-zA-Z0-9\s]'
    text=re.sub(pattern,' ',text)
    return text



def loadStop():
    sword = open("spam/stopwords.pkl" , "rb")
    sword = pickle.load(sword)
    return sword

def loadModel():
    clf = open("spam/cl3.pkl" , "rb")
    clf = pickle.load(clf)
    return clf

def loadVec():
    vec = open("spam/vec.pkl" , "rb")
    vec = pickle.load(vec)
    return vec


# remove stopwords
def removeStop(text):
    stop = loadStop()
    text = [x for x in text if x not in stop]
    return ''.join(text)
