# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm


def ta1109(c):
    if c == 1:
        b = np.array([[8., 4., 8.], [2., 10., 4.], [6., 2., 6.]], dtype=float)
    elif c == 2:
        b = np.array([[4., 5., 7.], [1., 8., 3.], [9., 0., 12.]], dtype=float)
    bbt = np.dot(b, np.transpose(b))
    btb = np.dot(np.transpose(b), b)
    print('v2=bbt=', bbt)
    v = sqrtm(bbt)
    print('v=', v)
    print('u2=btb=', btb)
    u = sqrtm(btb)
    print('u=', u)
    q = np.dot(b, np.linalg.inv(u))
    print('q=b*u-1=', q)
    q = np.dot(np.linalg.inv(v), b)
    print('q=v-1*b=', q)


ta1109(2)
