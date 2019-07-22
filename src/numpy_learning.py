# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 21:44
# @Author  : Wang Yibo
# @Email   : 171860683@smail.nju.edu.cn
# @File    : demo.py
# @Software: PyCharm

import sys
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

running = True


def main1():
    '''Return the result of two numbers.

    You can input two numbers, and you will get different result.
    '''
    global running
    while running:
        a, b = map(int, input('Please input two numbers').split())
        if a == 1 and b == 2:
            print('{0}+{1} = {2}'.format(a, b, (a + b)))
            running = False
        elif a == 3 and b == 4:
            print('{0}*{1} = {2}'.format(a, b, (a * b)))
            running = False
        else:
            print('{0}-{1} = {2}'.format(a, b, (a - b)))
    else:
        print("while is done")

    print('The command line arguments are:')
    for i in sys.argv:
        print(i)
    print('\n\nThe pythonpath is', sys.path, '\n')


def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


'''
if __name__ == '__main__':
    print(total(10, 1, 2, 3, vegetables=50, fruits=100))
    print(main.__doc__)
    main()
'''


def numpy_test():
    np.arange(5)
    a = np.arange(9)
    # print(np.arange(7, dtype='D'))
    print(a[3:7])
    print(a[::2])
    print(a[:7:2])
    print(a[::-1])

    b = np.arange(24).reshape(2, 3, 4)
    print('b.reshape: \n', b)
    print('b.ravel: \n', b.ravel())                     # 多维变一维，返回的是数组的视图，也就是说数组并没有被重新改变存储空间，只是当前视图是一维的
    print('b.flatten: \n', b.flatten())                 # 多维变一维，返回的是真实的数组，原来的数组被重新分配空间，之后返回新的数组
    b.shape = (6, 4)
    print('b.shape: \n', b)                             # 用元组定义数组形状
    print('b.transpose(): \n', b.transpose())           # 转置数组
    b.resize((2, 12))                                   # 改变数组的形状
    print('b.resize((2,12)): \n', b)

    c = np.arange(9).reshape(3, 3)
    print('c : \n', c)
    d = 2 * c
    print('d : \n', d)
    print('hstack : \n', np.hstack((c, d)))              # 水平叠加数组
    print('vstack : \n', np.vstack((c, d)))              # 垂直叠加数组
    print('concatenate : \n', np.concatenate((c, d), axis=1))    # axis = 1 水平叠加;   axis = 0 垂直叠加;
    print('dstack : \n', np.dstack((c, d)))                # 深度叠加数组

    oned = np.arange(2)
    twice_oned = 2 * oned
    print('row_stack((oned, twice_oned)) : \n', np.row_stack((oned, twice_oned)))                  # 以行方式对数组堆叠
    print('conlumn_stack((oned, twice_oned)) : \n', np.column_stack((oned, twice_oned)))           # 以列方式对数组堆叠
    print('np.row_stack((c, d)) == np.vstack((c, d)\n', np.row_stack((c, d)) == np.vstack((c, d))) # 比较row_stack 和  vstack
    print('np.column_stack((c, d)) == np.hstack((c, d))\n', np.column_stack((c, d)) == np.hstack((c, d)))   # 比较column_stack 和 hstack

    # 拆分与堆叠类似， hsplit, vsplit, dsplit
    e = np.arange(16).reshape(4, 4)
    print('e : \n', e)
    print('hsplit: \n', np.hsplit(e, 2))                 # parameter2 表示横向拆分的组数
    print('vsplit: \n', np.vsplit(e, 2))                 # parameter2 表示纵向拆分的组数

    f = np.arange(27).reshape(3, 3, 3)
    print('f = \n', f)
    print('dsplict: \n', np.dsplit(f, 3))                # parameter2 表示深度拆分的组数

    print('e.T = \n', e.T)                               # e的转置
    print('e.T == e.transpose \n', e.T == e.transpose())

def lena_pic():
    lena = scipy.misc.ascent()
    acopy = lena.copy()
    aview = lena.view()
    plt.subplot(221)
    plt.imshow(lena)

    plt.subplot(222)
    plt.imshow(acopy)

    plt.subplot(223)
    plt.imshow(aview)

    aview.flat = 0
    plt.subplot(224)
    plt.imshow(aview)
    plt.show()

def main():
    # numpy_test()
    lena_pic()

if __name__ == '__main__':
    main()
