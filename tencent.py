# -*- coding: utf-8 -*-
# Time       : 2019/4/5 19:31
# Author     : tangdaye
# Description: 腾讯笔试
import sys


def question1():
    def merge(nums1, nums2):
        t = []
        for n in nums1:
            t += max(nums1.count(n), nums2.count(n)) * [n]
        for n in nums2:
            t += max(nums1.count(n), nums2.count(n)) * [n]
        return t

    m, n = sys.stdin.readline().strip().split()
    m, n = int(m), int(n)
    coins = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        coins.append(int(line.strip()))
    dp = [[[]] * (m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(1, 1 + m):
            if i == 0:
                dp[i][j] = [coins[i]] * (j // coins[i]) if j % coins[i] == 0 else -1
            else:
                if sum(dp[i][j - 1]) >= j:
                    dp[i][j] = dp[i][j - 1]
                k = j // coins[i]
                m = dp[i][j - 1]

                for t in range(k, -1, -1):
                    if not dp[i - 1][j - k * coins[i]] == [-1]:
                        t = k * [coins[i]] + dp[i - 1][j - k * coins[i]]
                        temp = merge()
                    if not dp[i][j]:
                        dp[i][j] = [-1]
    result_map = {}
    for c in coins:
        result_map[c] = 0
    for t in dp[-1]:
        if t == [-1]:
            return -1
        if sum([k * v for k, v in result_map.items()]) >= sum(t):
            continue
        for c in coins:
            if t.count(c) > result_map[c]:
                result_map[c] = t.count(c)
    print(sum(result_map.values()))


def question2():
    m = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    k1, k2 = s.count('0'), s.count('1')
    print(len(s) - 2 * k1 if k1 <= k2 else len(s) - 2 * k2)


def question3():
    n = int(sys.stdin.readline().strip())

    pass


if __name__ == '__main__':
    question2()
