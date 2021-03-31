class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self


# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()


# print(sum(FirstHundredIterable()))
#
# for i in FirstHundredIterable():
#     print(i)

print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return  len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)


my_numbers = [x for x in [1, 2, 3]]  # iterator
my_numbers_gen = (x for x in [1, 2, 3])  # generator

print(next(my_numbers_gen))
