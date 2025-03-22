def multiples(n):
    for i in range(n):
        yield i ** 2

gen = multiples(5)
print(list(gen))
