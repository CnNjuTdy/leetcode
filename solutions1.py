# -*- coding: utf-8 -*-
# Time       : 2018/12/28 12:24 AM
# Author     : tangdaye
# Description: leetcode solutions 1-10

"""
1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def question1(nums, target):
    # nums = [2, 7, 11, 15]
    # target = 9
    my_map = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in my_map:
            return [my_map[target - num], i]
        else:
            my_map[num] = i


"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        result = ''
        while node is not None:
            result += str(node.val) + '->'
            node = node.next
        return result[:-2]


def question2(l1, l2):
    # l1 = ListNode(1)
    # l1.next = ListNode(8)
    # l1.next.next = ListNode(3)
    # l2 = ListNode(0)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    root = ListNode(0)
    current = root
    add_flag = 0
    while l1 and l2:
        r = l1.val + l2.val + add_flag
        if r >= 10:
            r, add_flag = r - 10, 1
        else:
            add_flag = 0
        current.next = ListNode(r)
        current = current.next
        l1 = l1.next
        l2 = l2.next
    if add_flag == 1:
        if l1:
            current.next = question2(l1, ListNode(1))
        elif l2:
            current.next = question2(l2, ListNode(1))
        else:
            current.next = ListNode(1)
    else:
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
    return root.next


"""
3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def question3(s):
    current, max_length = '', 0
    for char in s:
        if char not in current:
            current += char
            t = len(current)
            if t > max_length:
                max_length = t
        else:
            current = current[current.index(char) + 1:] + char
    return max_length


"""
4. 寻找两个有序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""


def question4(nums1, nums2):
    def get_i(l1, l2, start, end):
        m, n = len(l1), len(l2)
        i = int((start + end) / 2)
        j = int((m + n + 1) / 2 - i)
        if 0 < i and l1[i - 1] > l2[j]:
            return get_i(l1, l2, start, i)
        elif i < m and l2[j - 1] > l1[i]:
            return get_i(l1, l2, i + 1, end)
        else:
            return i

    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m
    i = get_i(nums1, nums2, 0, m)
    j = int((m + n + 1) / 2 - i)
    if i == 0:
        max_of_left = nums2[j - 1]
    elif j == 0:
        max_of_left = nums1[i - 1]
    else:
        max_of_left = max(nums1[i - 1], nums2[j - 1])

    if (m + n) % 2 == 1:
        return max_of_left

    if i == m:
        min_of_right = nums2[j]
    elif j == n:
        min_of_right = nums1[i]
    else:
        min_of_right = min(nums1[i], nums2[j])

    return (max_of_left + min_of_right) / 2.0


"""
5. 最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


def question5(s):
    n = len(s)
    centers = []
    for i in range(2 * n - 1):
        if i % 2 == 0:
            centers.append(s[i // 2])
        else:
            x, y = s[(i - 1) // 2], s[(i + 1) // 2]
            if x == y:
                centers.append(x + y)
            else:
                centers.append(None)
    for i in range(2 * n - 1):
        center = centers[i]
        if center:
            if i % 2 == 0:
                index, t = i // 2, 1
                while index - t >= 0 and index + t < n and s[index - t] == s[index + t]:
                    t += 1
                centers[i] = s[index - t + 1:index + t]
            else:
                index1, index2, t = (i - 1) // 2, (i + 1) // 2, 1
                while index1 - t >= 0 and index2 + t < n and s[index1 - t] == s[index2 + t]:
                    t += 1
                centers[i] = s[index1 - t + 1:index2 + t]
    max_str = ''
    for i in range(2 * n - 1):
        center = centers[i]
        if center:
            if len(center) > len(max_str):
                max_str = center
    return max_str


"""
6、 Z字形变换

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
"""


def question6(s, numRows):
    # array = [[None for j in range(len(s))] for i in range(numRows)]
    if numRows == 1:
        return s
    array = [[] for i in range(numRows)]
    row, should_up = 0, False
    for char in s:
        array[row].append(char)
        if row == 0:
            row += 1
            should_up = False
        elif row == numRows - 1:
            row -= 1
            should_up = True
        else:
            if should_up:
                row -= 1
            else:
                row += 1
    result = ''
    for row in array:
        result += ''.join(row)
    return result


"""
7. 整数翻转

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def question7(x):
    if x >= 0:
        x_str = str(x)
        t = int(x_str[::-1])
        return t if t <= 2 ** 31 - 1 else 0
    else:
        x_str = str(x)[1:]
        t = int(x_str[::-1])
        return -t if -t >= -2 ** 31 else 0


"""
8. 字符串转整数

请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 
"""


def question8(s):
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def my_abs(s, flag=True):
        result = 0
        for char in s:
            if char in l:
                index = l.index(char)
                result = result * 10 + index
                if flag and result > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                if not flag and result > 2 ** 31:
                    return 2 ** 31
            else:
                break
        if flag and result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if not flag and result > 2 ** 31:
            return 2 ** 31
        return result

    s = s.strip()
    if len(s) == 0:
        return 0
    if s[0] == '+':
        return my_abs(s[1:], True)
    elif s[0] == '-':
        return -my_abs(s[1:], False)
    elif s[0] in l:
        return my_abs(s, True)
    else:
        return 0


"""
9. 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


def question9(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]


"""
10. 正则表达式匹配

给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""


def question10(s, p):
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            elif p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[len(s)][len(p)]


if __name__ == '__main__':
    print(question10('aab', 'c*a*b'))
