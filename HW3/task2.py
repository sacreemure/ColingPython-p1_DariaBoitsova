from nltk import word_tokenize

class FileReader:
  def __init__(self, path):
    self.path = path
  
  
  def __add__(self, other):
      newfile = open('addresult.txt')
      with open(newfile, 'w') as i:
        for line in i:
          newfile.write(line)
      with open(other.path, 'w') as f:
        for line in f:
          newfile.write(line)
      return FileReader(newfile)

  def __str__(self):
    return f'{self.path}'
  
  def read(self):
    try:
      with open(self.path) as read_file:
        return read_file.read()
    except FileNotFoundError:
      return ''
  
  def write(self):
    try:
      with open(self.path, 'w') as write_file:
        write_file.write()
    except FileNotFoundError:
      return ''
    
  def count(self):
    l_count = 0
    w_count = 0
    for line in open(self.path):
      l_count += 1
      w_count += len(nltk.word_tokenize(line))
    return l_count, w_count
