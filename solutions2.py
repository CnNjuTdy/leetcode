# -*- coding: utf-8 -*-
# Time       : 2019/1/9 2:16 PM
# Author     : tangdaye
# Description: leetcode solutions 11-20

"""
11. 盛最多水的容器

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


def question11(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        this_area = min(height[l], height[r]) * (r - l)
        max_area = max_area if max_area >= this_area else this_area
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


"""
12. 整数转罗马数字

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。


示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


def question12(num):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'),
               (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'),
               (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    current = num
    result = ''
    for (al_num, roma_num) in num_map:
        while current >= al_num:
            result += roma_num
            current -= al_num
    return result


"""
12. 罗马数字转整数
"""


def question13(s):
    num_map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
               'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    result, i = 0, 0
    while i < len(s):
        if s[i:i + 2] in num_map:
            result += num_map[s[i:i + 2]]
            i += 2
        else:
            result += num_map[s[i]]
            i += 1
    return result


"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


def question14(strs):
    if not strs:
        return ""
    # if len(strs) == 1:
    #     return strs[0]
    s = strs[0]
    length = len(s)
    i = 1
    result = ''
    while i <= length:
        result = s[:i]
        for temp in strs:
            if not temp[:i] == result:
                return s[:i - 1]
        i += 1
    return result


"""
15. 三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。


满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def question15(nums):
    num_map = {}
    new_nums = []
    result = []
    for num in nums:
        if num not in num_map:
            num_map[num] = 1
        elif num == 0 and num_map[num] < 3:
            num_map[num] += 1
        elif (not num == 0) and num_map[num] == 1:
            num_map[num] += 1
    for num, count in num_map.items():
        new_nums += [num] * count
    new_nums.sort()
    length = len(new_nums)
    if length < 3:
        return result
    else:
        k = length - 1
        while k >= 2:
            target = -new_nums[k]
            i, j = 0, k - 1
            while i < j:
                if new_nums[i] + new_nums[j] < target:
                    i += 1
                elif new_nums[i] + new_nums[j] > target:
                    j -= 1
                else:
                    if [new_nums[i], new_nums[j], -target] not in result:
                        result.append([new_nums[i], new_nums[j], -target])
                    i += 1
                    j -= 1
            k -= 1
        return result


"""
16. 最接近的三数之和

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


def question16(nums, target):
    nums.sort()
    length = len(nums)
    k = length - 1
    result = []
    while k >= 2:
        new_target = target - nums[k]
        i, j = 0, k - 1
        min_abs = new_target - nums[i] - nums[j]
        while i < j:
            temp = new_target - nums[i] - nums[j]
            if temp < 0:
                j -= 1
                min_abs = min_abs if abs(min_abs) < -temp else temp
            elif temp > 0:
                i += 1
                min_abs = min_abs if abs(min_abs) < temp else temp
            else:
                return target
        result.append(min_abs)
        k -= 1
    result_min = result[0]
    for min_abs in result:
        result_min = result_min if abs(result_min) < abs(min_abs) else min_abs
    return target - result_min


"""
17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


def question17(digits):
    def list_mul(l1, l2):
        result = []
        for str1 in l1:
            for str2 in l2:
                result.append(str1 + str2)
        return result

    if not digits:
        return []
    num_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = ['']
    for i in digits:
        result = list_mul(result, num_map[i])
    return result


"""
18. 四数之和

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def question18(nums, target):
    length = len(nums)
    result = []
    if length < 4:
        return []
    nums.sort()
    for m in range(length - 3):
        for n in range(m + 1, length - 2):
            new_target = target - nums[m] - nums[n]
            i, j = n + 1, length - 1
            while i < j:
                current = nums[i] + nums[j]
                if current < new_target:
                    i += 1
                elif current > new_target:
                    j -= 1
                else:
                    temp = [nums[m], nums[n], nums[i], nums[j]]
                    if temp not in result:
                        result.append(temp)
                    i += 1
                    j -= 1
    return result


"""
19. 删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
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


def question19(head, n):
    # if not head.next:
    #     return None
    current1, current2 = head, head
    last = ListNode(-1)
    last.next = head
    head1 = last
    for i in range(n):
        current2 = current2.next
    while current2:
        last = last.next
        current1 = current1.next
        current2 = current2.next
    last.next = current1.next
    return head1.next


"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


def question20(s):
    map = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    i, stack = 0, [None]
    while i < len(s):
        if s[i] in map:
            stack.append(s[i])
        else:
            t = stack.pop()
            if not t or not map[t] == s[i]:
                return False
        i += 1
    return len(stack) == 1


if __name__ == '__main__':
    print(question20('[(])'))
