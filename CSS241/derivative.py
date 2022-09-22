import numpy as np


def derivative(f, x, n, h, d[i,j]):
    if n == 0:
        return f(x)
    else:
        return (derivative(f, x+h, n-1, h) - derivative(f, x-h, n-1, h))/(2*h)
