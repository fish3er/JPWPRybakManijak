class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

licznik = Counter(5)
print(next(licznik))
print(next(licznik))
print(next(licznik))
print(next(licznik))
print(next(licznik))
