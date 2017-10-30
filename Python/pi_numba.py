#!/usr/bin/env python3

from random import random
from time import time

from numba import jit

@jit
def sample_sum() -> int:
    sum = 0
    for _ in range(0, n):
        x = random()
        y = random()
        if x * x + y * y <= 1:
            sum += 1
    return sum

if __name__ == "__main__":
    n = 10_000_000
    start_time = time()
    pi = 4.0 * sample_sum() / n
    end_time = time()
    print('\tNumba: π ≅ {:.11f}, calculated in {:.2f}s, using {:,d} points.'.format(pi, end_time - start_time, n))
