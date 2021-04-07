import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def powers(limit):
    return [x**2 for x in range(limit)]


measure_runtime(lambda: powers(500000))  # 0.22379279136657715


# print(powers(5))
#
#
# start = time.time()
# powers(500000)
# end = time.time()
#
# print(end - start)  # 0.21729087829589844


import timeit


print(timeit.timeit("[x**2 for x in range(10)]"))  # 4.385567695
print(timeit.timeit("list(map(lambda x: x **2, range(10)))"))  # 5.094676309

