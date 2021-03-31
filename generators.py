def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


# print(hundred_numbers())
# print([x * 2 for x in hundred_numbers()])

# function remembers where it stopped
g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))  # starts from 2 - where we stopped


my_range_obj = range(10)
print(my_range_obj.__repr__()) #range(0, 10)
print(my_range_obj) #range(0, 10)


def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime

