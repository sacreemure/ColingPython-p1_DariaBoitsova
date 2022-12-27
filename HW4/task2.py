class ReverseIter(object):

    def __init__(self, items: list) -> None:
        self.items = items
        self.num = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num -= 1
        return self.items[num]
      
it = ReverseIter([10, 54, 12, 0])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
