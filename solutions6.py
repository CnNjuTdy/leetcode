# -*- coding: utf-8 -*-
# Time       : 2019/2/23 1:43 PM
# Author     : tangdaye
# Description: leetcode solutions 51-60

"""
51. N皇后问题
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""


def question51(n):
    def queen(A, l, cur=0):
        if cur == n:
            l.append(A.copy())
            return 0
        for col in range(n):
            A[cur], flag = col, True
            for row in range(cur):
                if A[row] == col or abs(col - A[row]) == cur - row:
                    flag = False
                    break
            if flag:
                queen(A, l, cur + 1)

    l = []
    queen([None] * n, l, 0)
    result = []
    for solution in l:
        temp = []
        for t in solution:
            temp.append(t * '.' + 'Q' + (n - 1 - t) * '.')
        result.append(temp)
    return result


def question52(n):
    def queen(A, l, cur=0):
        if cur == n:
            l.append(A.copy())
            return 0
        for col in range(n):
            A[cur], flag = col, True
            for row in range(cur):
                if A[row] == col or abs(col - A[row]) == cur - row:
                    flag = False
                    break
            if flag:
                queen(A, l, cur + 1)

    l = []
    queen([None] * n, l, 0)
    return len(l)


"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


def question53(nums):
    max_sum = -float("inf")
    last_max = 0
    for i in range(len(nums)):
        this_max = last_max + nums[i] if last_max > 0 else nums[i]
        last_max = this_max
        max_sum = max_sum if max_sum > this_max else this_max
    return max_sum


"""
54. 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""


def question54(matrix):
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    if m == 1:
        return matrix[0]
    if n == 1:
        return [row[0] for row in matrix]
    result = []
    times = m // 2 if m < n else n // 2
    i, j = 0, -1
    for i in range(times):
        next_i, next_j = 0, 1
        for _ in range(n):
            i, j = i + next_i, j + next_j
            result.append(matrix[i][j])
        next_i, next_j = 1, 0
        for _ in range(m - 1):
            i, j = i + next_i, j + next_j
            result.append(matrix[i][j])
        next_i, next_j = 0, -1
        for _ in range(n - 1):
            i, j = i + next_i, j + next_j
            result.append(matrix[i][j])
        for _ in range(m - 2):
            next_i, next_j = -1, 0
            i, j = i + next_i, j + next_j
            result.append(matrix[i][j])
        m, n = m - 2, n - 2
    if m == 1 and n == 1:
        result.append(matrix[i][j + 1])
    elif m == 1:
        for t in range(n):
            result.append(matrix[i][j + 1 + t])
    elif n == 1:
        for t in range(m):
            result.append(matrix[i + t][j + 1])
    return result


"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""


def question55(nums):
    length = len(nums)
    if length == 1:
        return True

    nums = nums[:-1]
    length -= 1
    i = length - 1
    while i >= 0:
        t = nums[i]
        if i + t >= length:
            nums = nums[:i]
            length = i
        i -= 1
    return len(nums) == 0


"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d,%d]' % (self.start, self.end)


def question56(intervals):
    def do_merge(result_map, interval, continue_flag=True):
        continue_flag = False
        for k, v in result_map.items():
            if k <= interval[0] <= interval[1] <= v:
                continue_flag = False
                break
            elif k <= interval[0] <= v <= interval[1]:
                result_map.pop(k)
                interval = [k, interval[1]]
                continue_flag = True
                break
            elif interval[0] <= k <= interval[1] <= v:
                result_map.pop(k)
                interval = [interval[0], v]
                continue_flag = True
                break
            elif interval[0] <= k <= v <= interval[1]:
                result_map.pop(k)
                continue_flag = True
                break
        if continue_flag:
            do_merge(result_map, interval, continue_flag)
        else:
            result_map[interval[0]] = interval[1]
            return

    result_map = {}
    result = []
    for interval in intervals:
        merge = 0
        for k, v in result_map.items():
            if k <= interval.start <= interval.end <= v:
                merge = 1
                break
            elif k <= interval.start <= v <= interval.end:
                merge = 2
                # result_map[k] = interval.end
                break
            elif interval.start <= k <= interval.end <= v:
                merge = 2
                # result_map.pop(k)
                # result_map[interval.start] = v
                break
            elif interval.start <= k <= v <= interval.end:
                merge = 2
                break
        if merge == 0:
            result_map[interval.start] = interval.end
        elif merge == 2:
            do_merge(result_map, [interval.start, interval.end])

    for k, v in result_map.items():
        result.append(Interval(k, v))
    return result


"""
57. 插入区间

给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


示例 1:
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
"""


def question57(intervals, newInterval):
    def merge(intervals, newInterval):
        continue_index, continue_interval = 0, None
        for i, interval in enumerate(intervals):
            x1, x2, y1, y2 = interval.start, interval.end, newInterval.start, newInterval.end
            if x1 <= x2 < y1 <= y2:
                continue_index = i + 1
                continue_interval = None
            elif y1 <= y2 < x1 <= x2:
                continue_index = i
                continue_interval = None
                break
            elif x1 <= y1 <= y2 <= x2:
                continue_index = -1
                break
            elif x1 <= y1 <= x2 <= y2:
                continue_index = i
                continue_interval = Interval(x1, y2)
                break
            elif y1 <= x1 <= x2 <= y2:
                continue_index = i
                continue_interval = newInterval
                break
            elif y1 <= x1 <= y2 <= x2:
                continue_index = i
                continue_interval = Interval(y1, x2)
                break
        if continue_index >= 0 and continue_interval:
            intervals.pop(continue_index)
            merge(intervals, continue_interval)
        elif continue_index >= 0 and not continue_interval:
            intervals.insert(continue_index, newInterval)

    merge(intervals, newInterval)
    return intervals


"""
58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

实例
输入: "Hello World"
输出: 5
"""


def question58(s):
    s = s.strip()
    if not s:
        return 0
    return len(s.split()[-1])


"""
59. 螺旋矩阵II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def question59(n):
    if not n:
        return []
    k = n - 1
    result = [[0] * n for _ in range(n)]
    num = 1
    while k >= 1:
        start_x, start_y = (n - k) // 2, (n - k) // 2
        end_x, end_y = n - 1 - (n - k) // 2, n - 1 - (n - k) // 2
        for i in range(4 * k):
            if i < k:
                result[start_x][start_y + i] = num
            elif i < 2 * k:
                result[start_x + i - k][end_y] = num
            elif i < 3 * k:
                result[end_x][end_y - (i - 2 * k)] = num
            elif i < 4 * k:
                result[end_x - (i - 3 * k)][start_y] = num
            num += 1
        k -= 2
    if k == 0:
        result[n // 2][n // 2] = num
    return result


"""
60. 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:
输入: n = 3, k = 3
输出: "213"
"""


def question60(n, k):
    if not n:
        return ""
    nums = list(range(1,n + 1))
    fa = [1] * (n + 1)
    s = ''
    for i in range(1, n + 1):
        fa[i] = fa[i - 1] * i
    i = n - 1
    while i >= 0:
        index = (k - 1) // fa[i]
        m = nums[index]
        s += str(m)
        k = k % fa[i]
        nums.remove(m)
        i -= 1
    return s


if __name__ == '__main__':
    x = question60(3, 6)
    print(x)
