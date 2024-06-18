# https://projecteuler.net/problem=1

from numba import jit
from utils import time_it


@time_it
def list_comprehension(target: int):
    return sum([x for x in range(1, target) if x % 3 == 0 or x % 5 == 0])

@time_it
def loop(target: int):
    total = 0
    for i in range(1, target):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

@time_it
@jit(nopython=True)
def loop_with_numba(target: int):
    total = 0
    for i in range(1, target):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Compile Numba
loop_with_numba(0)                # took: 0.1368 sec

# Test
# loop(1_000_000_000)             # took: 56.0389 sec
# loop_with_numba(1_000_000_000)  # took: 1.1940 sec

# Solve problem
print(loop_with_numba(1_000))     # 233168
