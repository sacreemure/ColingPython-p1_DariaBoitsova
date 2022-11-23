from nltk import word_tokenize

class FileReader():

    def __init__(self, path='str'):
        self.path = path

    def __str__(self):
        print(self.path)

    def __add__(self, other):
        newfile = open('addresult.txt', mode='w+', encoding='utf-8')
        try:
            with open(self.path, encoding='utf-8') as f:
                text = f.readlines()
                newfile.writelines(text)
            with open(other.path, encoding='utf-8') as g:
                text_2 = g.readlines()
                newfile.writelines(text_2)
            newfile.close()
            return FileReader('addresult.txt')
        except FileNotFoundError:
            newfile.close()
            print('Some of your files do not exist!')



    def read(self):
        try:
            with open(self.path, encoding='utf-8') as f:
                text = f.readlines()
                for i in text:
                    print(i)
        except FileNotFoundError:
            print('There is no such file in your directory!')
            return('')

    
    def write(self, line='str'): 
        try:
            with open(self.path, mode='a', encoding='utf-8') as f:
                f.write(line)
        except FileNotFoundError:
            print('There is no such file in your directory!')


    def count(self):
        try:
            self.line_count = 0
            self.word_count = 0
            with open(self.path, encoding='utf-8') as f:
                for line in f:
                    self.line_count += 1
                    self.word_count += len(word_tokenize(line))
        except FileNotFoundError:
            print('There is no such file in your directory!')




