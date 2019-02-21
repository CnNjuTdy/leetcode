# -*- coding: utf-8 -*-
# Time       : 2019/2/15 1:01 PM
# Author     : tangdaye
# Description: leetcode solutions 31-40
import math

"""
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


def question31(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return
    for i in range(len(nums) - 2, -1, -1):
        # 从后向前找到第一个比前一个大的数的位置
        if nums[i] < nums[i + 1]:
            # 第i个和后面最后一个比它大的交换位置
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            # 第i+1个向后逆转
            temp_length = len(nums) - i - 1
            for j in range(i + 1, i + 1 + math.ceil(temp_length / 2)):
                nums[j], nums[i - j] = nums[i - j], nums[j]
            return
    nums.reverse()
    return


"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


def question32(s):
    def find(s, c):
        sum_length, current_length, validate_length, max_length = 0, 0, 0, 0
        if c == '(':
            x = range(len(s))
        else:
            x = range(len(s) - 1, -1, -1)
        for i in x:
            t = s[i]
            if t == c:
                sum_length += 1
            else:
                sum_length -= 1
            current_length += 1
            if sum_length < 0:
                max_length = max_length if max_length > validate_length else validate_length
                sum_length, current_length, validate_length = 0, 0, 0
            elif sum_length == 0:
                validate_length = current_length
        return max_length if max_length > validate_length else validate_length

    x = find(s, '(')
    y = find(s, ')')
    return x if x > y else y


"""
33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


def question33(nums, target):
    def search_order(nums, target):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        index = len(nums) // 2
        if nums[index - 1] >= target:
            return search_order(nums[:index], target)
        else:
            x = search_order(nums[index:], target)
            return index + x if x > -1 else -1

    def search_no(nums, target):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        index = len(nums) // 2  # index>=1
        if nums[0] <= nums[index - 1]:
            if nums[index] <= nums[-1]:
                # 两边都有序
                if nums[index - 1] >= target >= nums[0]:
                    return search_order(nums[:index], target)
                else:
                    x = search_order(nums[index:], target)
                    return index + x if x > -1 else -1

            else:
                # 左边有序右边无序
                if nums[index - 1] >= target >= nums[0]:
                    return search_order(nums[:index], target)
                else:
                    x = search_no(nums[index:], target)
                    return index + x if x > -1 else -1
        else:
            # 左边无序右边有序
            if nums[index] <= target <= nums[- 1]:
                x = search_order(nums[index:], target)
                return index + x if x > -1 else -1
            else:
                return search_no(nums[:index], target)

    return search_no(nums, target)


"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


def question34(nums, target):
    def search_order(nums, target):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        index = len(nums) // 2  # index>=1
        if target < nums[index - 1]:
            return search_order(nums[:index], target)
        if target > nums[index - 1]:
            x = search_order(nums[index:], target)
            return [index + x[0], index + x[1]] if not x == [-1, -1] else [-1, -1]
        else:
            if target == nums[index - 1]:
                pass
                # 找到前面第一个target
                i, j = 0, 0
                for i in range(index - 1, -1, -1):
                    if not nums[i] == target:
                        break
                for j in range(index, len(nums)):
                    if not nums[j] == target:
                        break
                if i == 0 and nums[0] == target:
                    i -= 1
                if j == len(nums) - 1 and nums[-1] == target:
                    j += 1
                return [i + 1, j - 1]
            # 找到后面最后一个target
            else:
                return search_order(nums[:index], target)

    return search_order(nums, target)


"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
"""


def question35(nums, target):
    if not nums:
        return 0
    i = 0
    while i < len(nums) and nums[i] < target:
        i += 1
    if i == len(nums):
        if nums[i - 1] == target:
            return i - 1
        else:
            return i
    return i


"""
36. 有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""


def question36(board):
    class Sudo:
        def __init__(self, nums):
            self._nums = nums

        # 第i，j个所属块
        def block(self, i, j):
            s, t = i // 3, j // 3
            x = []
            for m in range(s * 3, (s + 1) * 3):
                for n in range(t * 3, (t + 1) * 3):
                    x += self._nums[m][n]
            return x

        def is_ok(self, i=None, j=None):
            if i is not None and j is not None:
                target = self._nums[i][j]
                if target == '.':
                    return True, -1, -1
                for k in range(9):
                    if not k == j and self._nums[i][k] == target:
                        return False, i, j
                    if not k == i and self._nums[k][j] == target:
                        return False, i, j
                    if not k == (i % 3) * 3 + (j % 3) and self.block(i, j)[k] == target:
                        return False, i, j
                return True, -1, -1
            else:
                for s in range(9):
                    for t in range(9):
                        m = self.is_ok(s, t)
                        if not m[0]:
                            return False, s, t
                return True, -1, -1

        def set(self, i, j, num):
            pass

        def get(self, i, j):
            return self._nums[i][j]

    sudo = Sudo(board)
    return sudo.is_ok()[0]


"""
37. 解数独
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""


def question37(board):
    def dfs(board, row, col, block, i, j):
        while board[i][j] != '.' "":
            if j == 8:
                i, j = i + 1, 0
            else:
                j += 1
            if i == 9:
                return 1
        for num in range(1, 10):
            block_index = i // 3 * 3 + j // 3
            if not row[i][num] and not col[j][num] and not block[block_index][num]:
                board[i][j] = str(num)
                row[i][num] = 1
                col[j][num] = 1
                block[block_index][num] = 1
                if dfs(board, row, col, block, i, j):
                    return 1
                else:
                    row[i][num] = 0
                    col[j][num] = 0
                    block[block_index][num] = 0
                    board[i][j] = '.'

    # row第i行第j列表示board第i行当中有没有数字j（i从0到8，j从1到9）
    row = [[0 for _ in range(10)] for _ in range(9)]
    # column第i行第j列表示board第i列当中有没有数字j（i从0到8，j从1到9）
    col = [[0 for _ in range(10)] for _ in range(9)]
    # block第i行第j列表示board第i个块当中有没有数字j（i从0到8，j从1到9）
    block = [[0 for _ in range(10)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if not board[i][j] == '.':
                num = int(board[i][j])
                row[i][num] = 1
                col[j][num] = 1
                block_index = i // 3 * 3 + j // 3
                block[block_index][num] = 1
    dfs(board, row, col, block, 0, 0)


"""
38. 报数
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
"""


def question38(n):
    def say(num):
        if len(num) == 0:
            return ''
        else:
            t = num[0]
            k = 0
            while k < len(num) and num[k] == t:
                k += 1
            return str(k) + str(t) + say(num[k:])

    result = ['1']
    while n > len(result):
        t = result[-1]
        result.append(say(t))
    return result[n - 1]


"""
40. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


def question39(candidates, target):
    def combination_sum(candidates, target):
        while candidates:
            x = candidates.pop()
            if x <= target:
                candidates.append(x)
                break
        if not candidates:
            return []
        if len(candidates) == 1:
            if candidates[0] > target:
                return []
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]
            else:
                return []
        result = []
        t = candidates.pop()
        m = target // t
        if m > 0:
            result += combination_sum(candidates.copy(), target)
            for j in range(1, m + 1):
                y = target - j * t
                if y == 0:
                    result.append([t] * j)
                    continue
                temp = combination_sum(candidates.copy(), y)
                result += [x + [t] * j for x in temp]
        return result

    return combination_sum(candidates, target)


"""
41. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


def question40(candidates, target):
    def combination_sum(candidates, target, candidates_count):
        while candidates:
            x = candidates.pop()
            if x <= target:
                candidates.append(x)
                break
        if not candidates:
            return []
        if len(candidates) == 1:
            if candidates[0] > target:
                return []
            if target % candidates[0] == 0 and target // candidates[0] <= candidates_count[candidates[0]]:
                return [[candidates[0]] * (target // candidates[0])]
            else:
                return []
        result = []
        t = candidates.pop()
        m = min(target // t, candidates_count[t])
        if m > 0:
            result += combination_sum(candidates.copy(), target, candidates_count)
            for j in range(1, m + 1):
                y = target - j * t
                if y == 0:
                    result.append([t] * j)
                    continue
                temp = combination_sum(candidates.copy(), y, candidates_count)
                result += [x + [t] * j for x in temp]
        return result

    new_candidates = []
    candidates_count = {}
    candidates.sort()
    for m in candidates:
        if m not in candidates_count:
            new_candidates.append(m)
            candidates_count[m] = 1
        else:
            candidates_count[m] += 1
    return combination_sum(new_candidates, target, candidates_count)


if __name__ == '__main__':
    x = question40([10, 1, 2, 7, 6, 1, 5], 8)
    print(x)
