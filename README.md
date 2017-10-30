# π by Monte Carlo

This directory contains various implementations in various languages of the parallel problem of calculating
an approximation of the value of π using Monte Carlo approach.

The area of the unit circle, i.e the circle with radius 1, is π. By randomly selecting (x, y) coordinates in
the ranges, 0 ≤ x ≤ 1, 0 ≤ y ≤ 1, if the expression:
```tex
x^2 + y^2 ≤ 1.0
```
is true then the (x, y) point is in the quarter circle, otherwise it is outside. Summing the number of
points inside and dividing by the total generated is an approximation of π/4.  The more points tried, the
more accurate the approximation.

These codes were initially created for a presentation at PyConUK 2017, "On Big Computation and Python". The
video of the presentation is [on YouTube](https://www.youtube.com/watch?v=Gr6XBaGwetY).
