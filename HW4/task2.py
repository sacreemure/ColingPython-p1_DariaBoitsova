class ReverseIter(object):

    def __init__(self, items: list):
        self.items = items
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.num < len(self.items):
            num = -(self.num + 1)
            self.num += 1
            return self.items[num]
        else:
            raise StopIteration
        
      
        
it = ReverseIter([10, 54, 12, 0])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
