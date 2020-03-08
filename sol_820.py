#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/short-encoding-of-words/


class Solution:
    def minimumLengthEncoding(self, words):
        def sort_by_len(elem):
            return len(elem)
        words.sort(key=sort_by_len, reverse=True)
        # print(words)
        S = ""
        for w in words:
            if S.find( w+'#') >= 0:
                continue
            else:
                S = S + w + '#'
        return len(S)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumLengthEncoding(["time", "me", "bell"]))
    print(s.minimumLengthEncoding(["me", "time"]))
