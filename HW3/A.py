class OneIndexedList():

    def __init__(self, items=[]):
        self.array = items

    def __getitem__(self, key):
        return self.array[key-1]

    def __setitem__(self, key, value):
        self.array[key-1] = value
