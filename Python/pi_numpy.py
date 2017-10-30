#!/usr/bin/env python3

# Solution from Claus Aichinger from a corridor conversation at PyCon UK 2018.

from time import time

from numpy import float, int, random

if __name__ == "__main__":
    n = 10_000_000
    start_time = time()
    pi = 4.0 * ((random.random((2, n)) ** 2).sum(axis=0) <= 1.0).mean()
    end_time = time()
    print('\tNumpy: π ≅ {:.11f}, calculated in {:.2f}s using {:,d} points.'.format(pi, end_time - start_time, n))
