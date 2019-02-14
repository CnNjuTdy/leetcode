# -*- coding: utf-8 -*-
# Time       : 2019/1/10 5:25 PM
# Author     : tangdaye
# Description: leetcode solutions 21-30

"""
21. 合并两个有序链表

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode(object):
    def __str__(self):
        node = self
        result = ''
        while node is not None:
            result += str(node.val) + '->'
            node = node.next
        return result[:-2]

    def __init__(self, x):
        self.val = x
        self.next = None


def question21(l1, l2):
    current1, current2 = l1, l2
    result = ListNode(-1)
    current = result
    while current1 and current2:
        if current1.val < current2.val:
            current.next = ListNode(current1.val)
            current1 = current1.next
        else:
            current.next = ListNode(current2.val)
            current2 = current2.next
        current = current.next
    if current1:
        current.next = current1
    else:
        current.next = current2
    return result.next


"""
22. 括号删除

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

 例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def question22(n):
    ans = []

    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    backtrack()
    return ans


"""
23. 合并K个排序链表

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""


def question23(lists):
    result = ListNode(-1)
    current = result
    lists = [node for node in lists if node]
    while lists and len(lists) >= 0:
        i, this_min, this_index = 1, lists[0].val, 0
        while i < len(lists):
            if this_min > lists[i].val:
                this_min = lists[i].val
                this_index = i
            i += 1
        current.next = ListNode(this_min)
        current = current.next
        lists[this_index] = lists[this_index].next
        lists = [node for node in lists if node]
    return result.next


"""
24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

说明:
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


def question24(head):
    if not head:
        return None
    if not head.next:
        return head
    result = ListNode(-1)
    result.next = head
    last, left, right = result, head, head.next
    while right:
        next_left = left.next.next
        if not next_left:
            right.next = left
            last.next = right
            left.next = next_left
            return result.next
        next_right = next_left.next
        right.next = left
        last.next = right
        left.next = next_left
        last = left
        left = next_left
        right = next_right
    return result.next


"""
25. k个一组翻转链表

给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


def question25(head, k):
    def f(head):
        left, right = None, head
        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        return left

    if not head:
        return None
    if not head.next:
        return head
    if k == 1:
        return head
    start, end = head, head
    for i in range(k - 1):
        end = end.next
        if not end:
            return start
    temp = end.next
    end.next = None
    f(start)
    start.next = question25(temp, k)
    return end


"""
26. 删除排序数组中的重复项

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
"""


def question26(nums):
    last, result, index = None, 0, 0
    while index < len(nums):
        if not nums[index] == last:
            result += 1
            last = nums[index]
            index += 1
        else:
            nums.__delitem__(index)
    return result


"""
27. 移除元素

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
"""


def question27(nums, val):
    i, j = 0, 0
    while j < len(nums):
        if not nums[j] == val:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i


"""
28. 实现strStr()

实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回-1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


def question28(haystack, needle):
    length = len(needle)
    for i in range(len(haystack) + 1 - length):
        if haystack[i:i + length] == needle:
            return i
    return -1


"""
29. 两数相除

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
"""


def question29(dividend, divisor):
    def f(t1, t2):
        if t1 < t2:
            return 0
        temp = t2
        result = -1
        while temp <= t1:
            temp = temp << 1
            result += 1
        t1 = t1 - (temp >> 1)
        return (1 << result) + f(t1, t2)

    if dividend == 0:
        return 0
    flag = True
    if dividend > 0 and divisor > 0:
        pass
    elif dividend > 0 and divisor < 0:
        flag = False
        divisor = -divisor
    elif dividend < 0 and divisor > 0:
        flag = False
        dividend = -dividend
    else:
        divisor = -divisor
        dividend = -dividend
    result = f(dividend, divisor)
    if flag and result > ((1 << 31) - 1):
        return (1 << 31) - 1
    if not flag and result > (1 << 31):
        return (1 << 31) - 1
    return result if flag else -result


"""
30. 与所有单词相关联的字串

给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:
输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
"""


def question30(s, words):
    def set_true(words, all, word):
        for i in range(len(words)):
            if words[i] == word and not all[i]:
                all[i] = True
                return True
        return False

    if not s or not words:
        return []
    n = len(words)
    length = len(words[0])
    if len(s) < n * length:
        return []
    indexes = []
    for index in range(len(s) + 1 - length):
        if s[index:index + length] in words:
            indexes.append(index)
    for index in indexes.copy():
        for i in range(n):
            if index + i * length not in indexes:
                indexes.remove(index)
                break
    result = []
    for index in indexes:
        count, all = 0, [False] * n
        for i in range(n):
            word = s[index + i * length:index + (i + 1) * length]
            if not set_true(words, all, word):
                break
            else:
                count += 1
            if count == n:
                result.append(index)

    return result


if __name__ == '__main__':
    pass