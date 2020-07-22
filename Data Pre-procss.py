from nltk.tokenize import RegexpTokenizer
from nlppreprocess import NLP
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

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
    3. Stemming or Leammatization (as per your requirement)"""
    
    processed_data = []
    
    for text in data:
        
        text = text.lower()
        tokens = ' '.join(i for i in tokenizer.tokenize(text))
        stopword = (nlp.process(tokens)).split()
        
        if key == 'stemmimg':
            stemming = [sb.stem(w) for w in stopword]
            processed_data.append(stemming)
        else:
            lemmatization = [lm.lemmatize(w) for w in stopword]
            processed_data.append(lemmatization)

    return processed_data
