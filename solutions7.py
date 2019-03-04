# -*- coding: utf-8 -*-
# Time       : 2019/3/1 9:01 AM
# Author     : tangdaye
# Description: leetcode 61-70
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        t = []
        current = self
        while current:
            t.append(current.val)
            current = current.next
        return t.__str__()


"""
61. 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
"""


def question61(head, k):
    root = ListNode(None)
    root.next = head
    current, length = root, 0
    while current.next:
        length += 1
        current = current.next
    if not length:
        return head
    k = length - k % length
    if k == length:
        return head
    last = current
    current, t = root, 0
    while current:
        if t == k:
            next_node = current.next
            root.next = next_node
            last.next = head
            current.next = None
            break
        else:
            pass
        current = current.next
        t += 1
    return root.next


"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
"""


def question62(m, n):
    if m < n:
        m, n = n, m
    # return C(m+n-2,n-1)
    x, y = 1, 1
    for i in range(0, n - 1):
        x *= (m + n - 2 - i)
        y *= (n - 1 - i)
    return x // y


"""
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
"""


def question63(obstacleGrid):
    # f(i,j) = f(i+1,j)+f(i,j+1)
    # if obstacleGrid[0][0]:
    #     return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    f = [[0] * n for _ in range(m)]
    # 初始化最后一行和最后一列
    for i in range(m - 1, -1, -1):
        if not obstacleGrid[i][n - 1]:
            f[i][n - 1] = 1
        else:
            break
    for j in range(n - 1, -1, -1):
        if not obstacleGrid[m - 1][j]:
            f[m - 1][j] = 1
        else:
            break
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            right = obstacleGrid[i][j + 1]
            down = obstacleGrid[i + 1][j]
            if obstacleGrid[i][j]:
                f[i][j] = 0
            elif right and down:
                f[i][j] = 0
            elif right:
                f[i][j] = f[i + 1][j]
            elif down:
                f[i][j] = f[i][j + 1]
            else:
                f[i][j] = f[i + 1][j] + f[i][j + 1]
    return f[0][0]


"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


def question64(grid):
    # dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    m, n = len(grid), len(grid[0])
    for i in range(1, m):
        grid[i][0] = grid[i - 1][0] + grid[i][0]
    for j in range(1, n):
        grid[0][j] = grid[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[- 1][- 1]


"""
65. 有效数字
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
"""


def question65(s):
    s = s.strip()
    try:
        t = float(s)
        return True
    except Exception:
        return False


"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def question66(digits):
    length = len(digits)
    add = 1
    for i in range(length - 1, -1, -1):
        if digits[i] + add == 10:
            digits[i] = 0
            add = 1
        else:
            digits[i] += add
            add = 0
            break
    if add:
        digits = [1] + digits
    return digits


"""
67. 二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
"""


def question67(a, b):
    (a, b) = (a, b) if len(a) >= len(b) else (b, a)
    m, n = len(a), len(b)
    i, j = m - 1, n - 1
    result, add = '', 0
    while i >= 0 and j >= 0:
        s, t = (int(a[i]) + int(b[j]) + add) % 2, (int(a[i]) + int(b[j]) + add) // 2
        add = t
        result = str(s) + result
        i, j = i - 1, j - 1
    if not add:
        result = a[:i + 1] + result
    else:
        while i >= 0:
            s, t = (int(a[i]) + add) % 2, (int(a[i]) + add) // 2
            add = t
            result = str(s) + result
            i -= 1
        if add == 1:
            result = '1' + result
    return result


"""
68. 文本左右对齐
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。

示例:
输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


def question68(words, maxWidth):
    i = 0
    result = []
    while i < len(words):
        this_line = [words[i]]
        this_min_length = len(words[i])
        j = i + 1
        while this_min_length < maxWidth:
            if j == len(words):
                j += 1
                this_line.append('')
                break
            this_min_length += 1 + len(words[j])
            this_line.append(words[j])
            j += 1
        i = j - 1
        result.append(this_line[:-1])
    result2 = []
    for i, line in enumerate(result):
        x = ''
        blanks = maxWidth - sum([len(word) for word in line])
        if i == len(result) - 1:
            x = ' '.join(result[-1]) + (blanks - len(result[-1]) + 1) * ' '

        else:
            t = len(line) - 1
            if t > 0:
                for word in line[:-1]:
                    m = math.ceil(blanks / t)
                    x += word + ' ' * m
                    t -= 1
                    blanks -= m
            x += line[-1] + blanks * ' '
        result2.append(x)
    return result2


"""
69. 平方根

实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2
示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""


def question69(x):
    return int(x ** 0.5)


"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


def question70(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    # node1.next.next = ListNode(2)
    print(question70(2))
