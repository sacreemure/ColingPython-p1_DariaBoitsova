import pickle
from typing import List
from tqdm import tqdm
from corus import load_corpora


class UnigramMorphAnalyzer:

    def __init__(self):
        self.stats = {}
        self.train_data = []
        self.eval_data = []
        file_name = 'pos_data.txt'

    def __getitem__(self, x):
        return self.stats[x]

    def save(self):
      with open('p_statistics.pkl', 'wb') as file:
        pickle.dump(self.stats, file)

    def load(self):
      with open('p_statistics.pkl', 'rb') as file:
        self.stats = pickle.load(file)
        return self.stats

    def train(self, x, y):
        for word in x:
            for i in range(4, 0, -1):
                ending = word[-i:]
                if word not in self.stats:
                    if ending not in self.stats:
                        self.stats[ending] = {}
                    elif tag not in self.stats[y]:
                        self.stats[ending][tag] = 1
                    else:
                        self.stats[ending][tag] += 1
        return stats   

    def predict(self, x: List[str]):
        if not self.stats:
            stats = self.load()
        else:
            stats = self.stats
        ending = x[-min(len(x), 4):]
        try:
            total = sum(stats[ending].values())
            final_stats = {}
            for tag, value in stats[ending].items():
                probability = value / total
                final_stats[tag] = probability
        except KeyError:
            return {0: 0}
        return dict(sorted(final_stats.items(), key=lambda item: item[1], reverse=True))
       

    def eval(self, x, y):
        correct = 0
        for word, tag in zip(x, y):
            pred = self.predict(word)
            if word == tag:
                correct += 1
        return correct / len(y)

if __name__ == '__main__':
    tagger = UnigramMorphAnalyzer()
