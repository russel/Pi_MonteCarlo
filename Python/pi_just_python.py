#!/usr/bin/env python3

from random import random
from time import time

def f() -> int:
    x = random()
    y = random()
    return 1 if x * x + y * y <= 1 else 0

if __name__ == "__main__":
    n = 10_000_000
    start_time = time()
    pi = 4.0 * sum(f() for _ in range(0, n)) / n
    end_time = time()
    print('\tJust Python: π ≅ {:.11f}, calculated in {:.2f}s, using {:,d} points.'.format(pi, end_time - start_time, n))
