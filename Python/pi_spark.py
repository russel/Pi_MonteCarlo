#!/usr/bin/env python3

"""Calculate π using a Monte Carlo approach

Randomly select a large number of points in the unit square and count how many
are inside the x^2 + y^2 <= 1. This gives an estimate for π/4.

Usage: pi [partitions]
"""

# This code is an amendment of https://github.com/apache/spark/blob/master/examples/src/main/python/pi.py

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from random import random
from operator import add
from time import time

from pyspark.sql import SparkSession

def f(_: int) -> int:
    x = random()
    y = random()
    return 1 if x ** 2 + y ** 2 <= 1 else 0

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    n = 10_000_000
    start_time = time()
    count = spark.sparkContext.parallelize(range(0, n), partitions).map(f).reduce(add)
    end_time = time()
    print('\tSpark: π ≅ {:.11f}, calculated in {:.2f}s, using {:,d} points.'.format(4.0 * count / n, end_time - start_time, n))
    spark.stop()
