from nltk.tokenize import RegexpTokenizer
from nlppreprocess import NLP
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import gc

gc.disable()

tokenizer = RegexpTokenizer("[a-zA-Z]+",)
stopwords = NLP()  #for stopwords removal
sb = SnowballStemmer('english')
lm = WordNetLemmatizer()

def get_preocessed_data(data,key='stemming'):
    
    """This function is a pipeline to exatract relevant 
    and useful data for our further operation.
    
    Here we will process our data with 3 important process.
    1. Tokenization
    2. Stopwords Removal
    3. Stemming or Lemmatization (as per your requirement)"""
    
    processed_data = []
    
    for text in data:
        
        text = text.lower()
        text = ' '.join(i for i in tokenizer.tokenize(text))
        text = (stopwords.process(text)).split()
        
        if key == 'stemming':
            text = [sb.stem(w) for w in text]
            text = ' '.join(w for w in text)
            processed_data.append(text)
        else:
            text = [lm.lemmatize(w) for w in text]
            text = ' '.join(w for w in text)
            processed_data.append(text)

    return processed_data
