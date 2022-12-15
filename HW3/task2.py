import nltk

class FileReader:
  def __init__(self, path):
    self.path = path
    
  def read(self):
    return ""
  
  def write(self):
  
  def count(self):
    l_count = 0
    w_count = 0
    for line in open(self.path):
      # returns an iterator
      l_count += 1
      w_count += len(nltk.word_tokenize(line))
      
  def __add__(self, other):
    return FileReader("")
  
FileReader("a.txt") + FileReader("b.txt")

