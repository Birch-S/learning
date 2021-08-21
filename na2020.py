# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def na233_11():
    a = [[-0.002, 2, 2], [1, 0.78125, 0], [3.996, 5.5625, 4]]
    b = [[0.4], [1.3816], [7.4178]]
    a = np.asarray(a)
    b = np.asarray(b)
    """列主元消元法"""
    x = naf1(a, b)
    print(x)
    # print(np.matmul(a, x) - b)


def naf1(a, b):
    """列主元消元法"""
    n = np.size(b)  # 确定维数
    ab = np.concatenate((a, b), axis=1)  # 增广矩阵
    x = np.zeros(n)  # 为解分配内存
    for kk in range(0, n - 1):
        i_k = np.argmax(abs(ab[kk:, kk])) + kk  # 寻找主元
        temp = np.copy(ab[i_k, :])
        ab[i_k, :] = np.copy(ab[kk, :])
        ab[kk, :] = temp  # 行交换
        if ab[kk, kk] == 0:
            exit('sorry, a_kk=0')  # 主元为零时退出报错
        # print(ab)
        for ii in range(kk + 1, n):
            ab[ii, :n + 1] -= ab[kk, :n + 1] / ab[kk, kk] * ab[ii, kk]  # Gauss消元
        # print(ab)

    for kk in range(n - 1, -1, -1):
        x[kk] = 1 / ab[kk, kk] * (ab[kk, n] - np.dot(x[kk + 1:], ab[kk, kk + 1:n]))  # 求解x

    return x.reshape(n, 1)


# na233_11()


def na233_14():
    a = [[16, 4, 8], [4, 5, -4], [8, -4, 22]]
    b = [[-4], [3], [10]]
    a = np.asarray(a)
    b = np.asarray(b)
    x = naf2(a, b)
    print(x)
    # print(np.matmul(a, x) - b)
    """平方根法"""


def naf2(a, b):
    """平方根法"""
    n = np.size(b)  # 确定维数
    l_ij = np.zeros((n, n))
    y = np.zeros(n)  # 为中间变量分配内存
    x = np.zeros(n)  # 为解分配内存

    for jj in range(0, n - 1):
        l_ij[jj, jj] = np.sqrt(a[jj, jj] - np.dot(l_ij[jj, :jj], l_ij[jj, :jj]))
        if l_ij[jj, jj] == 0:
            exit('sorry, l_kk=0')  # 主元为零时退出
        for ii in range(jj + 1, n):
            l_ij[ii, jj] = (a[ii, jj] - np.dot(l_ij[ii, :jj], l_ij[jj, :jj])) / l_ij[jj, jj]
    l_ij[n - 1, n - 1] = np.sqrt(a[n - 1, n - 1] - np.dot(l_ij[n - 1, :n - 1], l_ij[n - 1, :n - 1]))
    if l_ij[n - 1, n - 1] == 0:
        exit('sorry, l_kk=0')  # 主元为零时退出

    for kk in range(0, n):
        y[kk] = 1 / l_ij[kk, kk] * (b[kk] - np.dot(y[:kk], l_ij[kk, :kk]))  # 求解y

    for kk in range(n - 1, -1, -1):
        x[kk] = 1 / l_ij[kk, kk] * (y[kk] - np.dot(x[kk + 1:], l_ij[kk + 1:, kk]))  # 求解x

    return x.reshape(n, 1)


# na233_14()


def na234_16():
    a = [[240, -319.5], [-179.5, 240]]
    b = [[3], [4]]
    ai = np.linalg.inv(a)
    x = np.dot(ai, b)
    print(x)
    print(sum(ai, 0))

    a = [[240, -319], [-179, 240]]
    b = [[3], [4]]
    ai = np.linalg.inv(a)
    x = np.dot(ai, b)
    print(x)
    print(sum(ai, 0))

    print(559.0 * 1.12024)
    print(626.2*0.5/559*4/(1-626.2*0.5/559))


na234_16()
