# -*- coding: utf-8 -*-
# Time       : 2019/3/5 10:30 AM
# Author     : tangdaye
# Description: leetcode 71-80

"""
71. 简化路径

以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
"""


def question71(path):
    stack = []
    for t in path.split('/'):
        if t:
            if t == '.':
                pass
            elif t == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(t)
    return '/' + '/'.join(stack)


"""
72. 编辑距离

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""


def question72(word1, word2):
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
    return dp[-1][-1]


"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""


def question73(matrix):
    m = len(matrix)
    if not m:
        return
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if 0 == matrix[i][j]:
                for k in range(m):
                    matrix[k][j] = None if not matrix[k][j] == 0 else 0
                for k in range(n):
                    matrix[i][k] = None if not matrix[i][k] == 0 else 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    return


"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
"""


def question74(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    i, j = 0, len(matrix) - 1
    if not matrix[i][0] <= target <= matrix[j][-1]:
        return False
    while i < j - 1:
        line = (i + j) // 2
        if matrix[line][0] <= target <= matrix[j][-1]:
            i = line
        elif matrix[i][0] <= target <= matrix[line][-1]:
            j = line
    index = -1
    if i < j:
        if matrix[i][0] <= target <= matrix[i][-1]:
            index = i
        elif matrix[i][-1] < target < matrix[j][0]:
            return False
        else:
            index = j
    t, i, j = matrix[index], 0, len(matrix[index]) - 1
    while i <= j:
        k = (i + j) // 2
        if t[k] == target:
            return True
        elif target < t[k]:
            j = k - 1
        else:
            i = k + 1
    return False


"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
注意:
不能使用代码库中的排序函数来解决这道题。
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


def question75(nums):
    def quick3(nums, l, r):
        if l >= r:
            return
        lt = l  # [l+1,lt]<v
        gt = r + 1  # [gt,r]>v
        i = l + 1
        v = nums[l]
        while i < gt:
            if nums[i] < v:
                nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
                lt += 1
                i += 1
            elif nums[i] > v:
                nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
                gt -= 1
            else:
                i += 1
        nums[l], nums[lt] = nums[lt], nums[l]
        quick3(nums, l, lt - 1)
        quick3(nums, gt, r)

    l = 0
    r = len(nums)
    quick3(nums, l, r - 1)
    print(nums)


"""
76. 最小覆盖子串
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""


def question76(s, t):
    res = []
    if not s or len(s) < len(t):
        return ''
    t_d = {}
    for c in t:
        if c in t_d:
            t_d[c] += 1
        else:
            t_d[c] = 1
    i, j = 0, 0
    count = 0  # 找到的字符个数
    tmp_min = len(s) + 1  # 目前最小值
    while j < len(s):
        if s[j] in t_d:
            t_d[s[j]] -= 1
            if t_d[s[j]] >= 0:
                count += 1
        while count == len(t):
            if (j - i + 1) < tmp_min:
                tmp_min = j - i + 1
                res = s[i:j + 1]
            if s[i] in t_d:
                t_d[s[i]] += 1
                if t_d[s[i]] > 0:
                    count -= 1
            i += 1
        j += 1
    return res


"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


def question77(n, k):
    import itertools
    return list(itertools.combinations(range(1, n + 1), k))


"""
78. 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def question78(nums):
    def f(l, index, result):
        if index == len(nums):
            temp = []
            for i in range(len(nums)):
                if l[i]:
                    temp.append(nums[i])
            result.append(temp)
        else:
            l[index] = 1
            f(l, index + 1, result)
            l[index] = 0
            f(l, index + 1, result)

    result = []
    l = [0] * len(nums)
    f(l, 0, result)
    return result


"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""


def question79(board, word):
    def f(path, word):
        if not word:
            return True
        c = word[0]
        if not path:
            for m in range(len(board)):
                for n in range(len(board[0])):
                    if board[m][n] == c:
                        if f(path + [[m, n]], word[1:]):
                            return True
        else:
            x, y = path[-1]
            for m, n in [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]:
                if 0 <= m < len(board) and 0 <= n < len(board[0]) and [m, n] not in path and board[m][n] == c:
                    if f(path + [[m, n]], word[1:]):
                        return True
        return False

    path = []
    return f(path, word)


"""
80. 删除排序数组中的重复项 II
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。
"""


def question80(nums):
    i = 0
    for e in nums:
        if i < 2 or e != nums[i - 2]:
            nums[i] = e
            i += 1
    return i


if __name__ == '__main__':
    print(question79([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCCED'))
