from typing import Any, Callable

import numpy as np
from numpy.linalg import *
import torch as t
from torch import nn
from torch.autograd import Variable as V
import matplotlib.pyplot as plt


def python1026():
    """单引号和双引号"""
    str1 = "I'm a great coder!"  # 使用双引号包围含有单引号的字符串
    str2 = '引文双引号是"，中文双引号是“'  # 使用单引号包围含有双引号的字符串
    print(str1)
    print(str2)
    print('英文单引号\'中文单引号‘中文双引号“英文双引号"')
    print('a', '\t', 'a')

    a = {'one': 1, 'two': 2, 'three': 3}  # a是一个字典类型
    print(type(a))


# python1026()


def python0120():
    """闭包函数和lambda函数"""

    # 闭包函数，其中 exponent 称为自由变量
    def nth_power(exponent):
        def exponent_of(base):
            return base ** exponent

        return exponent_of  # 返回值是 exponent_of 函数

    square = nth_power(2)  # 计算一个数的平方
    cube = nth_power(3)  # 计算一个数的立方
    print(square(2))  # 计算 2 的平方
    print(cube(2))  # 计算 2 的立方

    power = lambda x, y: x ** y
    print(power(2, 10))
    print(power(3, 3))


# python0120()


def python0121():
    '''class'''

    class Animal:
        def __init__(self, age):
            self.age = age

        def disp_age(self):
            print("the animal's age is", self.age)

    class People:
        def __init__(self, name):
            self.name = name

        def disp_name(self):
            print("the people's name is", self.name)

    class Student:
        def __init__(self, grade):
            self.grade = grade

        def disp_grade(self):
            print("the student is in ", self.grade)

    class Customer:
        def __init__(self, shopping):
            self.shopping = shopping

        def disp_shopping(self):
            print("the costume want to buy", self.shopping)

    class Sb(Animal, People, Student, Customer):
        def __init__(self, age, name, grade, shopping):
            Animal.__init__(self, age)
            People.__init__(self, name)
            Student.__init__(self, grade)
            Customer.__init__(self, shopping)

    zhangsan = Sb(8, 'zhangsan', 'Grade 4', 'book')
    zhangsan.disp_shopping()


# python0121()


def python0122():
    '''class'''

    class WhichSay:
        def say(self, which):
            which.say()

    class Animal:
        def __init__(self, age):
            self.age = age

        def say(self):
            print("the animal's age is", self.age)

    class People:
        def __init__(self, name):
            self.name = name

        def say(self):
            print("the people's name is", self.name)

    class Student:
        def __init__(self, grade):
            self.grade = grade

        def say(self):
            print("the student is in ", self.grade)

    class Customer:
        def __init__(self, shopping):
            self.shopping = shopping

        def say(self):
            print("the costume want to buy", self.shopping)

    a = WhichSay()
    a.say(Customer("a book"))  # which = Customer("a book")


# python0122()


def numpy1031():
    """ReLU和Sigmoid激活函数示意图"""
    # 设置图片大小
    plt.figure(figsize=(8, 3))

    # x是1维数组，数组大小是从-10. 到10.的实数，每隔0.1取一个点
    x = np.arange(-10, 10, 0.1)
    # 计算 Sigmoid函数
    s = 1.0 / (1 + np.exp(- x))

    # 计算ReLU函数
    y = np.clip(x, a_min=0., a_max=None)

    #########################################################
    # 以下部分为画图程序

    # 设置两个子图窗口，将Sigmoid的函数图像画在左边
    plt.subplot(121)
    # 画出函数曲线
    plt.plot(x, s, color='r')
    # 添加文字说明
    plt.text(-5., 0.9, r'$y=\sigma(x)$', fontsize=13)
    # 设置坐标轴格式
    current_axis = plt.gca()
    current_axis.xaxis.set_label_text('x', fontsize=15)
    current_axis.yaxis.set_label_text('y', fontsize=15)

    # 将ReLU的函数图像画在右边
    plt.subplot(122)
    # 画出函数曲线
    plt.plot(x, y, color='g')
    # 添加文字说明
    plt.text(-3.0, 9, r'$y=ReLU(x)$', fontsize=13)
    # 设置坐标轴格式
    current_axis = plt.gca()
    current_axis.xaxis.set_label_text('x', fontsize=15)
    current_axis.yaxis.set_label_text('y', fontsize=15)

    plt.show()


# numpy1031()


def torch1031():
    """tensor"""
    t.tensor([5.5, 3])
    t.empty(5, 3)
    t.zeros(5, 3, dtype=t.float32)
    t.zeros(5, 3, dtype=t.int64)
    x = t.zeros(5, 3)
    y = t.rand(5, 3)
    y.cuda()
    print(x.add(y), x)
    # print(x.add_(y), x)


# torch1031()


def torch0118():
    """Autograd"""
    x = V(t.arange(0, 3))
    b = V(t.rand(3), requires_grad=True)
    w = V(t.rand(3), requires_grad=True)
    y = w * x + 2 * b
    z = sum(y)
    print(z.requires_grad)
    print(z.grad_fn.next_functions)
    z.backward()
    print(w.grad)
    print(b.grad)
    print(t.autograd.grad(z, y))


# torch0118()


def torch0119():
    """Regression"""
    t.manual_seed(1000)

    def get_fake_data(batch_size=10):
        """产生随机数据：y = x * 2 + 3, 加上一些噪声"""
        x = t.rand(batch_size, 1) * 20
        y = x * 2 + (1 + t.randn(batch_size, 1) * 0.4) * 3
        return x, y

    x, y = get_fake_data()
    plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
    plt.show()

    # 随机初始化参数
    w = V(t.rand(1, 1), requires_grad=True)
    b = V(t.zeros(1, 1), requires_grad=True)
    lr = 0.0002

    for ii in range(10000):
        x, y = get_fake_data()
        x, y = V(x), V(y)

        y_pred = x.mm(w) + b.expand_as(y)
        loss = 0.5 * (y_pred - y) ** 2
        loss = loss.sum()
        loss.backward()
        w.data.sub_(lr * w.grad.data)
        b.data.sub_(lr * b.grad.data)

        w.grad.data.zero_()
        b.grad.data.zero_()

        if ii % 1000 == 0:
            print(w.data.squeeze().numpy(), b.data.squeeze())


# torch0119()


def torch0816():
    x = V(t.Tensor([0, 1, 2]), requires_grad=True)
    y = x ** 2 + x * 2
    # z = sum(y)
    y_grad_variables = V(t.Tensor([1, 1, 1]))
    y.backward(y_grad_variables)
    print(x.grad)


torch0816()
