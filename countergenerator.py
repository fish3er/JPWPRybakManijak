def counter(n):
    i = 0
    while i < n:
        yield i
        i += 1


licznik = counter(1000)
for i in range(1000):
    print(next(licznik))

