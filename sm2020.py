# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt


def sm1019():
    f = np.array([[2 / 3, 0, 0], [0, 1, -1 / np.sqrt(3)], [0, np.sqrt(2), 1 / 3]], dtype=float)
    sigma = 90 * np.array([[0, 0, 0], [0, 1, np.sqrt(3)], [0, np.sqrt(3), 0]], dtype=float)
    t = det(f) * np.dot(inv(f), sigma)
    s = np.dot(t, np.transpose(inv(f)))
    print('det(f)=', det(f))
    print('|f|=', (2 + 2 * np.sqrt(6)) / 9)
    print('f^(-1)=', inv(f))
    print('|t|=', t)
    print('|s|=', s)
    n = np.array([0, 1 / 2, np.sqrt(3) / 2], dtype=float)
    print(det(f) * np.sqrt(np.dot(np.dot(n, f), np.dot(n, f))))
    print(135 - 67.5 / 2)


# sm1019()
