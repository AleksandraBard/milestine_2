def starts_with_l(friend):
    return friend.startswith('l')



friends = ['sasha', 'bato', 'lena', 'kostya']
start_with_l = filter(starts_with_l, friends)

# print(next(start_with_l))
# print(next(start_with_l))
# print(next(start_with_l))

print(list(start_with_l))  # [lena]
print(list(start_with_l))  # []


siblings = ['sasha', 'bato', 'lena', 'kostya']
start_with_k = filter(lambda sibling: sibling.startswith('k'), siblings)

another_starts_with_k = (s for s in siblings if s.startswith('k'))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

