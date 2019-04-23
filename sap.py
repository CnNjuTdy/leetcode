# -*- coding: utf-8 -*-
# Time       : 2019/4/11 19:00
# Author     : tangdaye
# Description: SAP笔试题
import sys


def question1():
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    for i in range(n):
        a, b = [int(x) for x in sys.stdin.readline().strip().split()]
        print(m + a - b if m + a - b > 0 else 0)


def combine(n, k):  # 计算C(n,k)
    if n < k:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i)
    for i in range(k):
        result /= (i + 1)
    return result


def question2():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    k1 = a.count(9)
    k2 = a.count(6)
    t1 = combine(n - k1 - k2, k)
    t2 = combine(n - k1 - k2, k - 1) * (k1 + k2)
    t3 = combine(n - k1 - k2, k - 2) * k1 * k2
    print(int(t1 + t2 + t3))


if __name__ == '__main__':
    # print(combine(4,2))
    question2()
    pass
