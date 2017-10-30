# π by Monte Carlo

This repository contains various implementations in various languages of the embarrassingly parallel problem
of calculating an approximation of the value of π using Monte Carlo approach.

The area of the unit circle, i.e the circle with radius 1, is π. By randomly selecting (x, y) coordinates in
the ranges, 0 ≤ x ≤ 1, 0 ≤ y ≤ 1, if the expression:
```tex
x^2 + y^2 ≤ 1.0
```
is true then the (x, y) point is in the quarter unit circle centred at (0, 0), otherwise it is
outside. The total of points inside divided by the total generated is an approximation of π/4.
The more points tried, the more accurate the approximation.

These codes were initially created for a presentation at PyConUK 2017, "On Big Computation and Python". The
video of the presentation is [on YouTube](https://www.youtube.com/watch?v=Gr6XBaGwetY).

Another code has been added after the session, a Numpy version suggested by Claus Aichinger via email
prompted by a conversation after the session.
