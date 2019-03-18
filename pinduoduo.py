# -*- coding: utf-8 -*-
# Time       : 2019/3/10 4:38 PM
# Author     : tangdaye
# Description: todo
import sys
import collections


def question1():
    n = int(sys.stdin.readline().strip())
    nums1 = [int(x) for x in sys.stdin.readline().strip().split()][:n]
    nums2 = [int(x) for x in sys.stdin.readline().strip().split()][:n]
    nums1.sort(reverse=True)
    nums2.sort()
    print(sum([nums1[i] * nums2[i] for i in range(n)]))


def question2():
    s = sys.stdin.readline().strip().lower()
    count = collections.Counter(s)
    stack = []
    visited = collections.defaultdict(bool)
    for c in s:
        count[c] -= 1
        if visited[c]:
            continue
        while stack and count[stack[-1]] and stack[-1] > c:
            visited[stack[-1]] = False
            stack.pop()
        visited[c] = True
        stack.append(c)
    print("".join(stack)[0])


def question3():
    n, d = [int(x) for x in sys.stdin.readline().strip().split()]
    bank_list = []
    for _ in range(n):
        x, y = sys.stdin.readline().strip().split()
        bank_list.append([int(x), int(y)])
    bank_list.sort(key=lambda x: x[1], reverse=True)
    this_max = float('-inf')
    for i in range(n - 1):
        if bank_list[i][1] + bank_list[i + 1][1] <= this_max:
            break
        for j in range(i + 1, n):
            if bank_list[i][0] - bank_list[j][0] >= d or bank_list[i][0] - bank_list[j][0] <= -d:
                t = bank_list[i][1] + bank_list[j][1]
                this_max = t if t > this_max else this_max
                break
    print(this_max)


def question4():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    length1, length2 = len(s1), len(s2)
    if (length1 + length2) % 2 == 0:
        print(19)
    else:
        print(0)


def f(s):
    x = 0
    for c in s:
        if c == '(':
            x += 1
        else:
            x -= 1
            if x < 0:
                return False
    return x == 0


if __name__ == '__main__':
    x = f('()()(()')
    print(x)
