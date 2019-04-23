# -*- coding: utf-8 -*-
# Time       : 2019/4/9 19:34
# Author     : tangdaye
# Description: 招商银行笔试 蔡莹玥
import sys


def question1():
    n, a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    k = n // c
    t = k // a
    print(k + t * b)


def question2():
    n, w = [float(x) for x in sys.stdin.readline().strip().split()]
    n = int(n)
    a = [float(x) for x in sys.stdin.readline().strip().split()]
    a.sort()
    t = min(a[0], a[n] / 2)
    print(min(3 * t * n, w))


if __name__ == '__main__':
    question2()
