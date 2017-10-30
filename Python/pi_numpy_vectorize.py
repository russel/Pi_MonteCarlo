#!/usr/bin/env python3

from time import time

from numpy import float, int, random, vectorize

def f(x: float, y: float) -> int:
    return 1 if x ** 2 + y ** 2 <= 1 else 0

if __name__ == "__main__":
    n = 10_000_000
    start_time = time()
    pi = 4.0 * vectorize(f)(random.random(n), random.random(n)).sum() / n
    end_time = time()
    print('\tNumpy Vectorize: π ≅ {:.11f}, calculated in {:.2f}s using {:,d} points.'.format(pi, end_time - start_time, n))
