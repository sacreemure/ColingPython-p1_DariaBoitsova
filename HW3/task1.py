class OneIndexedList:
  
  def __init__(self, items: list):
    self.items = [] or items
    
  def __getitem__(self, index: int):
    return self.items[index - 1]  
    
  def __setitem__(self, index: int, value: any):
    self.items[index - 1] = value
    
