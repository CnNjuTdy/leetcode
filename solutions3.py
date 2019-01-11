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


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    print(question25(node1, 3))
