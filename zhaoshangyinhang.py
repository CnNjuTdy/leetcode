# -*- coding: utf-8 -*-
# Time       : 2019/3/17 19:00
# Author     : tangdaye
# Description: 招商银行

import sys


def question1():
    n = int(sys.stdin.readline().strip())
    trees = []
    for _ in range(n):
        trees.append([int(x) for x in sys.stdin.readline().strip().split()])
    trees.sort(key=lambda x: x[0])
    if trees[0][0] > 0:
        print(trees[0][1])
        return
    elif trees[-1][0] < 0:
        print(trees[-1][1])
        return
    else:
        i = 0
        for i in range(n):
            if trees[i][0] > 0:
                break
        if n % 2 == 1:
            if i <= (n - 1) // 2:
                print(sum([x[1] for x in trees[:2 * i + 1]]))
                return
            elif i >= (n + 1) // 2:
                print(sum([x[1] for x in trees[2 * i - n - 1:]]))
                return
        else:
            if i < n // 2:
                print(sum([x[1] for x in trees[:2 * i + 1]]))
                return
            elif i == n // 2:
                print(sum([x[1] for x in trees]))
                return
            else:
                print(sum([x[1] for x in trees[2 * i - n - 1:]]))
                return


def question2():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    highs = [int(x) for x in sys.stdin.readline().strip().split()]
    t = min(highs)
    highs = [x - t for x in highs]
    import math
    print(math.ceil(sum(highs) / k))


def question3():
    n = int(sys.stdin.readline().strip())
    nums = [int(x) for x in sys.stdin.readline().strip().split()]
    # 删掉连续的0
    i = 0
    while i < n:
        if nums[i] == 0:
            j = i + 1
            while j < n and nums[j] == 0:
                nums.pop(j)
                n -= 1
            i = j
        else:
            i += 1
    print(sum([x if x > 0 else -x for x in nums]))
    # 先吃0

    # # 一共吃n-1次
    # for _ in range(n - 1):
    #     # 优先找异号
    #     index = 0
    #     for index in range(n - 1):
    #         if (nums[index] > 0 and nums[index + 1] < 0) or (nums[index] < 0 and nums[index + 1] > 0):
    #             break
    #     # 如果找到了
    #     if index < n - 2 or (index == n - 2 and ((nums[-2] > 0 and nums[-1] < 0) or (nums[-2] < 0 and nums[-1] > 0))):

    print(nums)


if __name__ == "__main__":
    question3()
