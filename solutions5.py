# -*- coding: utf-8 -*-
# Time       : 2019/2/20 7:01 PM
# Author     : tangdaye
# Description: leetcode solutions 41-50
"""
41. 缺失的第一个正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""


def question41(nums):
    if len(nums) == 0:
        return 1
    x = {}
    for num in nums:
        x[num] = 1
    i = 1
    while i < len(nums):
        if i in x:
            i += 1
        else:
            return i
    if i in x:
        return i + 1
    else:
        return i


"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


def question42(height):
    def trap(height):
        if not height:
            return 0
        max_index = height.index(max(height))
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        sum_origin, sum_update = 0, 0
        while i < max_index:
            sum_origin += height[i]
            if height[i] > left_max:
                left_max = height[i]
            sum_update += left_max
            i += 1
        while j > max_index:
            sum_origin += height[j]
            if height[j] > right_max:
                right_max = height[j]
            sum_update += right_max
            j -= 1
        return sum_update - sum_origin

    return trap(height)


def question43(num1, num2):
    if len(num1) > len(num2):
        num2 = "0" * (len(num1) - len(num2)) + num2
    else:
        num1 = "0" * (len(num2) - len(num1)) + num1
    str2int = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    int2str = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}
    length1, length2 = len(num1), len(num2)
    length = length1 + length2 - 1
    result = [0] * length
    for i in range(length):
        if i < length1:
            range_start = 0
            range_end = i + 1
        else:
            range_start = i - length1 + 1
            range_end = length1
        for s in range(range_start, range_end):
            t = i - s
            result[i] += str2int[num1[s]] * str2int[num2[t]]
    s = ''
    q = 0
    for i in range(length - 1, -1, -1):
        q, r = (result[i] + q) // 10, (result[i] + q) % 10
        s = int2str[r] + s
    if q > 0:
        s = int2str[q] + s
    for i in range(len(s)):
        if s[i] == 0:
            i += 1
        else:
            return s[i:]
    return "0"


if __name__ == '__main__':
    print(question43("9133", "0"))
