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


"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
"""


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


"""
44. 匹配字符串
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
"""


def question44(s, p):
    n = len(s)
    m = len(p)
    last = [False] * (n + 1)
    last[0] = True
    for i in range(m):
        if p[i] == '*':
            for j in range(n):
                last[j + 1] = last[j + 1] or last[j]
        elif p[i] == '?':
            del last[-1]
            last.insert(0, False)
        else:
            cur = [False]
            for j in range(n):
                cur.append(last[j] and p[i] == s[j])
            last = cur
    return last[-1]


"""
45. 跳跃游戏II
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""


def question45(nums):
    def find_index(nums, end, index_list):
        if end == 0:
            return
        i = 0
        while i <= end - 1:
            if i + nums[i] >= end:
                index_list.append(i)
                break
            i += 1
        find_index(nums, end=i, index_list=index_list)
        return

    n = len(nums)
    if n == 1:
        return 0

    end, index_list = n - 1, []
    find_index(nums, end, index_list)
    return len(index_list)


"""
46. 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""


def question46(nums):
    length = len(nums)
    if length == 0:
        return []
    nums.sort()
    result = [[nums[0]]]
    for i in range(1, length):
        for l in result:
            if len(l) == i:
                for j in range(i):
                    temp = l.copy()
                    temp.insert(j, nums[i])
                    result.append(temp)
                l.append(nums[i])
    return result


"""
47. 全排列II
给定一个可包含重复数字的序列，返回所有不重复的全排列
"""


def question47(nums):
    length = len(nums)
    if length == 0:
        return []
    nums.sort()
    result = [[nums[0]]]
    for i in range(1, length):
        for l in result:
            if len(l) == i:
                for j in range(i):
                    temp = l.copy()
                    temp.insert(j, nums[i])
                    result.append(temp)
                l.append(nums[i])
    t = []
    for l in result:
        if l not in t:
            t.append(l)
    return t


"""
48. 旋转图像
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""


def question48(matrix):
    n = len(matrix)
    if n == 1:
        return
    else:
        # 第i行放到倒数第i列上
        matrix[:] = [[matrix[n - i - 1][j] for i in range(n)] for j in range(n)]


"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


def question49(strs):
    result_map = {}
    for word in strs:
        word_list = list(word)
        word_list.sort()
        if str(word_list) not in result_map:
            result_map[str(word_list)] = [word]
        else:
            result_map[str(word_list)].append(word)
    result = list(result_map.values())
    return result


"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""


def question50(x, n):
    return x ** n


if __name__ == '__main__':
    print(question49(["eat", "tea", "tan", "ate", "nat", "bat"]))
