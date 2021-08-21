# encoding:utf-8
import numpy as np


def mc():
    cb = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
          ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
          ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A'],
          ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
          ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
          ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1'],
          ['2', '3', '4', '5', '6', '7', '8', '9', '~'],
          ['!', '@', '#', '$', '%', '^', '&', '*', '('],
          [')', '+', '-', '/', '<', '>', ';', ':', ' ']]

    cb = np.array(cb)

    en_or_de = input("选择需要进行加密还是解密: e/d?")
    if en_or_de == 'e':  # 加密
        m_word = input(u"请输入要加密的内容:")
        # m_word = m_word.replace(' ', '')  # 去空格
        print(m_word)
        # m_word = m_word.lower()  # 全部转为小写
        for c in m_word:
            idx = np.argwhere(cb == c)  # 将输入的字符串与密码本比较
            print(idx[0][0], end='')
            print(idx[0][1], end='')  # 输出行号和列号
    elif en_or_de == 'd':
        c_word = input(u"请输入密文:")
        for c in range(0, len(c_word), 2):  # 将输入的密文两位一断，再与密码本比较
            idx1 = int(c_word[c])  # 奇数位是行号
            idx2 = int(c_word[c + 1])  # 偶数位是列号
            print(cb[idx1][idx2], end='')  # 按行号和列号从密码本输出原字符


# mc()


def kaisa():
    n = 3  # 移动多少位
    cb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cb = np.array(cb)

    en_or_de = input("选择需要进行加密还是解密: e/d?")
    if en_or_de == 'e':  # 加密
        m_word = input(u"请输入要加密的内容:")
        m_word = m_word.replace(' ', '')  # 去空格
        m_word = m_word.lower()  # 全部转为小写
        print(m_word)
        for c in m_word:
            idx = np.argwhere(cb == c)  # 将原字符与密码本比较
            idn_new = (idx[0][0] + n) % 26  # 移动n位，并取模，得到加密后的索引
            print(cb[idn_new], end='')  # 按加密后的索引从密码本输出加密后的字符
    elif en_or_de == 'd':
        m_word = input(u"请输入密文:")
        for c in m_word:
            idx = np.argwhere(cb == c)  # 将加密的字符与密码本比较
            idn_new = (idx[0][0] - n) % 26  # 移动-n位，并取模，得到原字符的索引
            print(cb[idn_new], end='')  # 按原字符的索引从密码本输出原字符


kaisa()
