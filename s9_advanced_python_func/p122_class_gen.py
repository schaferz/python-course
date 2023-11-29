class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


gen = FirstHundredGenerator()
next(gen)  # 0
next(gen)  # 1


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


for i in FirstFiveIterator():
    print(i)
