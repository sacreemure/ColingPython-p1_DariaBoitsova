import pickle
from tqdm import tqdm


class UnigramMorphAnalyzer:

    def __init__(self):
        self.stats = {}
        self.train_data = []
        self.eval_data = []
        file_name = 'pos_data.txt'

    def __getitem__(self, token):
        return self.stats[token]

    def save(self):
      with open('p_statistics.pkl', 'wb') as file:
        pickle.dump(self.stats, file)

    def load(self):
      with open('p_statistics.pkl', 'rb') as file:
        self.stats = pickle.load(file)
        return self.stats

    def train(self, x, y):
       

    def predict(self, token: str):
       

    def eval(self, x, y):
        

if __name__ == '__main__':
    tagger = UnigramMorphAnalyzer()
    tagger.train()
    tagger.save()
    tagger.load()
    print(tagger.predict('спать'))
    print(tagger['ть'])
    print(tagger.eval())
