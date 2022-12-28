import pickle
from tqdm import tqdm

class UnigramMorphAnalyzer:
  def __init__(self):
    self.stats = {}
    
  def train(self, X, y):
    for word in X:
      for i in range(4, 0, -1):
        ending = word[-1:]
        if word not in self.stats:
          if ending not in self.stats:
            self.stats[ending] = {}
           
          if y not in self.stats[y]
  
  def predict(self, X: List[str]):
    return y
  
  def eval(self, X, y):
    return score
  
if __name__ == "__main__":
  tagger = UnigramMorphAnalyzer()
  

