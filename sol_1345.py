#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/jump-game-iv/
# 解题思路：宽搜 + 剪枝 (很有挑战性)

from collections import defaultdict

class Solution:
    def minJumps(self, arr):
        loc_d = defaultdict(list)
        n = len(arr)

        for i in range(n):
            loc_d[arr[i]].append(i)
        # print(loc_d)

        visited = [0] * n
        visited[0] = 1
        loc_step = [(0, 0)]
        while loc_step:
            idx, step = loc_step.pop(0)
            for i in loc_d[arr[idx]] + [idx-1, idx+1]:
                if i < 0 or i >= n or visited[i]:
                    continue
                if i == n-1:
                    return step + 1
                visited[i] = 1
                loc_step.append((i, step+1))
            loc_d[arr[idx]] = []
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
    print(s.minJumps([7]))
    print(s.minJumps([7,6,9,6,9,6,9,7]))
    print(s.minJumps([6,1,9]))
