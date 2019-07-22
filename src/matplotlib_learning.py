# @Time    : 2019/7/22 14:12
# @Author  : Wang Yibo
# @Email   : 171860683@smail.nju.edu.cn
# @File    : matplotlib.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


def line_test():
    x = np.linspace(0, 20)
    plt.plot(x, .5 + x)
    plt.plot(x, 1 + 2 * x, '--')
    plt.show()


def line_test2():
    data = np.arange(100, 201)
    plt.subplot(2, 1, 1)  # (2, 1, 1)表示一共有两行，这幅图在第一行第一列的位置
    plt.plot(data)

    data2 = np.arange(200, 301)
    plt.subplot(2, 1, 2)
    plt.plot(data2)

    plt.show()


def scater_test():
    N = 20  # 散点图
    # plt.scatter(x,y,color颜色,size大小,alpha透明度)
    plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='r', s=100, alpha=0.5)
    plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='g', s=200, alpha=0.5)
    plt.scatter(np.random.rand(N) * 100, np.random.rand(N) * 100, c='b', s=300, alpha=0.5)
    plt.show()


def pie_test():
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    data = np.random.rand(7) * 100

    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend()

    plt.show()


def bar_test():
    N = 7

    x = np.arange(N)
    data = np.random.randint(low=0, high=100, size=N)
    colors = np.random.rand(N * 3).reshape(N, -1)
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    plt.title("Weekday Data")
    plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)
    plt.show()


def hist_test():
    data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
    labels = ['3K', '4K', '5K']
    bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]

    plt.hist(data, bins=bins, label=labels)
    plt.legend()

    plt.show()


def matplotlib_test():
    ''' To make the plot display one window, you can choose one test to run.

    No parameter.
    '''
    # line_test()
    # line_test2()
    # scater_test()
    # pie_test()
    # bar_test()
    hist_test()

def main():
    matplotlib_test()


if __name__ == '__main__':
    main()
