#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/prison-cells-after-n-days/

# 解题思路：因为总共数组长度就为8，所以最多会出现2^8=256中组合，只要出现一次重复，后续必然全部相同。
#     因此该题必然会出现周期循环现象，故而优化的重点就在于找到周期 N = 14 了。


class Solution:
    def plus_one(self, cells):
        cell_ret = list()
        cell_ret.append(0)
        for i in range(1, 7):
            cur_state = int(cells[i-1] == cells[i+1])
            cell_ret.append(cur_state)
        cell_ret.append(0)
        return cell_ret

    def prisonAfterNDays(self, cells, N):
        if N <= 0:
            return cells
        N = N % 14
        if N == 0:
            N = 14
        temp_cells = cells
        for i in range(1, N+1):
            temp_cells = self.plus_one(temp_cells)
            # print(i, temp_cells)
        return temp_cells


if __name__ == "__main__":
    s = Solution()
    print(s.prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
    print(s.prisonAfterNDays([0,1,0,1,1,0,0,1], 16))
    # print(s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
