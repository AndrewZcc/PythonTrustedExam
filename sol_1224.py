#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/maximum-equal-frequency/

# 思路一：正向找前缀，直到找到 最后一个匹配的为止（超时, 29/42）
# 思路二：反向 从后向前找，找到第一个匹配的即可结束 (超时, 36/42)
# 思路三：继续 剪枝，在进行匹配时 记录已经比较过的次数相同的num，出现次数相同的 不需全部比较，只需比较一个即可。


class Solution:
    def is_same(self, states):
        if len(states) == 0:
            return True
        count, value = 0, 0
        for k, v in states.items():
            if v == 0:
                continue
            if count == 0:
                value = v
                count = 1
            else:
                if v != value:
                    return False
        return True

    def is_match(self, states):
        compared_v = list()
        for k, v in states.items():
            if v in compared_v:
                continue
            else:
                compared_v.append(v)
                states[k] -= 1
                if self.is_same(states):
                    return True
                states[k] += 1
        return False

    # method-2
    def maxEqualFreq(self, nums):
        states = dict()
        for num in nums:
            if num not in states.keys():
                states[num] = 1
            else:
                states[num] += 1

        count = 0
        nums.reverse()
        for num in nums:
            if self.is_match(states.copy()):
                break
            states[num] -= 1
            count += 1
        return len(nums) - count

    # method-1
    def maxEqualFreq_1(self, nums):
        # print(nums)
        states = dict()
        ret = 0
        for it in enumerate(nums):
            idx, num = it[0], it[1]
            if num not in states.keys():
                states[num] = 1
            else:
                states[num] += 1
            res = self.is_match(states.copy())
            if res:
                ret = idx + 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maxEqualFreq([2,2,1,1,5,3,3,5]))
    print(s.maxEqualFreq([2,2,1,1,5,3,3]))
    print(s.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
    print(s.maxEqualFreq([1,1,1,2,2,2]))
    print(s.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
