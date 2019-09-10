# -*- coding: utf-8 -*-
# Time       : 2019/4/24 19:46
# Author     : tangdaye
# Description: leetcode 81-90
"""
81. 搜索旋转排序数组II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
"""


def question81(nums, target):
    def binary_search(left, right, nums, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return False

    def sub_search(left, right, nums, target):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right]:
                for i in range(left, right + 1):
                    if nums[i] == target:
                        return True
                return False

            if nums[mid] >= nums[left]:  # 左边是有序的
                if nums[mid] > target >= nums[left]:  # target在左边
                    return binary_search(left, mid - 1, nums, target)
                else:
                    return sub_search(mid + 1, right, nums, target)
            elif nums[mid] <= nums[right]:  # 右边是有序的
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid + 1, right, nums, target)
                else:
                    return sub_search(left, mid - 1, nums, target)

        return False

    return sub_search(0, len(nums) - 1, nums, target)


"""
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def question82(head):
    if not head:
        return None
    stack = []
    current = head
    last_same = float("inf")
    while current:
        if stack and stack[-1] == current.val:
            while stack and stack[-1] == current.val:
                last_same = current.val
                stack.pop(-1)
        else:
            if not current.val == last_same:
                stack.append(current.val)
        current = current.next
    start = ListNode(None)
    current = start
    for t in stack:
        current.next = ListNode(t)
        current = current.next
    return start.next


"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""


def question83(head):
    if not head:
        return None
    last = ListNode(head.val - 1)
    last.next = head
    root = last
    current = head
    while current:
        if current.val == last.val:
            last.next = current.next
        else:
            last = current
        current = current.next
    return root.next

"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10
"""
def question84_1(heights):
    def f(heights,index):
        min_since_then,result = float('inf'),0
        i = index
        while i >= 0:
            min_since_then = min_since_then if min_since_then<=heights[i] else heights[i]
            result = result if result>= min_since_then*(index+1-i) else min_since_then*(index+1-i)
            i-=1
        return result
    dp,i = 0,0
    for i in range(len(heights)):
        t = f(heights,i)
        dp = t if t >= dp else dp
    return dp


    

"""
85. 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例：
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

输出: 6
"""


def question85(matrix):
    def f(martrix, p, q):
        result, max_height = 0, []
        j = 0
        while q - j >= 0 and martrix[p][q - j] == "1":
            i = 0
            while p - i >= 0 and martrix[p - i][q - j] == "1":
                i += 1
            max_height.append(i)
            j += 1
        min_since_then = float('inf')
        for i in range(1, len(max_height) + 1):
            x = max_height[i - 1]
            min_since_then = min_since_then if min_since_then <= x else x
            result = (result
                      if result >= min_since_then * i else min_since_then * i)
        return result

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = max(f(matrix, i - 1, j - 1), dp[i - 1][j],
                               dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == "__main__":
    # question85([['1','1','1','1'],['1','1','1','1'],['0','1','1','1']])
    x = question84([2,1,5,6,2,3])
    print(x)