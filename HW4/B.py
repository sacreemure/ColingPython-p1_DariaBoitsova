class ReverseIter():

    def __init__(self, array='list'):
        self.array = array
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.array):
            n = -(self.i + 1)
            self.i += 1
            return self.array[n]
        else:
            raise StopIteration()




