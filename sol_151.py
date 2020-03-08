#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# https://leetcode-cn.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

    def reverseWords_my(self, s):
        s_list = s.strip().split(' ')
        stripped_s = list()
        for str in s_list:
            if len(str):
                stripped_s.append(str)
        stripped_s.reverse()
        return ' '.join(stripped_s)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("a good   example"))
