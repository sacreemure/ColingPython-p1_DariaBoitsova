import pickle
import tqdm
from corus import load_corpora

class UnigramMorphAnalyser(): 

    def __init__(self):
        pass

    def train(self, path):
        
        self.path = path
        records = load_corpora(path)

        stats = {}
        stop_pos = ['LATN', 'NUMB', 'PNCT']

        for rec in tqdm.tqdm(records):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        for i in range(-4, 0):
                            token_text = token.text[i:]
                            token_pos = token.forms[0].grams[0]
                            if token_pos not in stop_pos:
                                if token_text in stats:
                                    if token_pos in stats[token_text]:
                                        stats[token_text][token_pos] += 1  
                                    else:
                                        stats[token_text][token_pos] = 1
                                else:
                                    stats[token_text] = {token_pos: 1}

        return stats

    def save(self, test_path):

        with open('model.pickle', 'wb') as handle:
            pickle.dump(self.train(test_path), handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):

        with open('model.pickle', 'rb') as handle:
            stats = pickle.load(handle)

        return stats

    def predict(self, token='str'):
        
        stats = self.load()

        final_stats = {}

        needed_range = min(4, len(token))

        for i in range(-needed_range, 0):
            token_text = token[i:]
            if token_text in stats:
                token_stats = stats[token_text]
                all_sum = sum(token_stats.values())
                for j in token_stats:
                    probability = token_stats[j] / all_sum
                    final_stats[j] = probability
            else:
                continue

        final_stats = dict(reversed(sorted(final_stats.items(), key=lambda item: item[1])))

        return final_stats

    def __getitem__(self, token):

        stats = self.load()
        return(stats[token])
        


    def eval(self, eval_path='str', model_path='str'):

        model = self.load(model_path)
        test_data = load_corpora(eval_path)

        counter = 0
        correct_counter = 0

        for rec in tqdm.tqdm(test_data):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        analyzer_data = self.predict(token.text)
                        if len(analyzer_data) > 0:
                            counter += 1
                            analyzer_output = list(analyzer_data)[0]
                            if analyzer_output == token.forms[0].grams[0]:
                                correct_counter += 1
                        else:
                            continue

        print(f"This morphanalyzer's correctness is {correct_counter/counter} with your test corpus")


 
if __name__ == '__main__':
    pass

