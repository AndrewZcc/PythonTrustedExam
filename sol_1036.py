#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/escape-a-large-maze/

# 解题思路一：一圈圈向外扩大搜索圈，直到搜到目标所在的圈为止（有点BFS的思想）【超时/一圈圈扩展太浪费时间】
# 解题思路二：从 src 和 dest 分别向外出发，搜索到的点的个数 超过 blocked.size 时 代表包不住了。 (21/26)

from collections import deque


class Solution:
    MAX = 10**6
    MIN = 0

    def outer(self, point):
        out_list = list()
        x, y = point[0], point[1]
        up, dw = [x, y+1], [x, y-1]
        lf, rf = [x-1, y], [x+1, y]
        if x+1 < self.MAX:
            out_list.append(rf)
        if x-1 >= self.MIN:
            out_list.append(lf)
        if y+1 < self.MAX:
            out_list.append(up)
        if y-1 >= self.MIN:
            out_list.append(dw)
        return out_list

    def isEscapePossible(self, blocked, source, target):
        if len(blocked) == 0:
            return True

        block_size = len(blocked)
        src_queue = deque()
        src_search = list()
        src_queue.append(source)
        dest_queue = deque()
        dest_search = list()
        dest_queue.append(target)

        while True:
            if len(src_queue) > 0:
                for p in self.outer(src_queue[0]):
                    if p not in blocked and p not in src_search:
                        src_queue.append(p)
                if target in src_queue:
                    return True
                src_search.append(src_queue.popleft())

            if len(dest_queue) > 0:
                for p in self.outer(dest_queue[0]):
                    if p not in blocked and p not in dest_search:
                        dest_queue.append(p)
                if source in dest_queue:
                    return True
                dest_search.append(dest_queue.popleft())
            if len(src_queue) == 0 or len(dest_queue) == 0:
                break

            if len(src_queue) > block_size and len(dest_queue) > block_size:
                return True
        return False

    def isEscapePossible_my(self, blocked, source, target):
        if len(blocked) == 0:
            return True
        queue_list = list()
        searched = list()
        queue_list.append(source)
        for point in queue_list:
            for p2 in self.outer(point):
                if p2 not in blocked and p2 not in searched:
                    queue_list.append(p2)
            if target in queue_list:
                return True
            searched.append(point)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.MAX)
    print(s.isEscapePossible([[0,1],[1,0]], [0,0], [0,2]))
    print(s.isEscapePossible([[0,1]], [0,0], [0,2]))
    print(s.isEscapePossible([[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
                            ,[655988,180910] ,[267728,840949]))
