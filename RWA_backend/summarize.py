
from factorsum.model import FactorSum
import collections as ct
import string
import nltk
import sys

if 'factorsum' not in sys.path:
    sys.path.append('factorsum')
    last_training_domain = None
    last_dataset = None
    last_split = None
 
try:
    nltk.data.find("tokenizers/punkt")
except:
    nltk.download("punkt", quiet=True)
 

class Summarizer:
    
    def __init__(self, domain = 'arxiv'):
        
      self.model = FactorSum(domain)

    def get_summary(self, document):
        summary = self.model.summarize(
                  document, # a document string 
                  target_budget=200,  
                  verbose=True,
              )
        res = self.filter_summary(summary[0])
        return res

    def filter_summary(self, summary):
        
        tmp = []

        punct =  string.punctuation.replace('.', '')
        punct =   punct.replace(',', '')
        punct =   punct.replace('?', '')
        punct =   punct.replace('!', '')
        punct =   punct.replace('.', '')
        # print(summary)
        
        for summ in summary:
           count  = sum(v for k, v in ct.Counter(summ).items() if k in punct)
        #    print(count)
           summ = summ[0].capitalize() + summ[1:]
           if(count < 5):
               tmp.append(summ)

        return " ".join(tmp)
  



 
         