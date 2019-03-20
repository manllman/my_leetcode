# !python3
# -*- coding:utf-8 -*- 
# @Author:Sqing
# @Time:2019年03月20日19:11
# TODO：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# ~~~~~~~~~~~~~~~~~~~~~~~

# 暴力解法
class S_1:
    def lengthOfLongestSubstring(self, s):
        '''
        :param s str:
        :return int:
        '''
        if s == "":
            return 0
        elif s == " ":
            return 1
        elif len(s)== 1:
            return 1

        s_list = list(s)
        result = []
        for i in range(len(s_list)-1):
            longest_sub_str = 1
            for j in range(i+1,len(s_list)):
                if s_list[j] not in s_list[i:j]:
                    longest_sub_str += 1
                else:break
            result.append(longest_sub_str)
        return max(result)

# S-2
# 字典元素出现的位置之差就是最长子串的长度
class S_2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(j-i+1,ans)
            st[s[j]] = j + 1
        return ans;

import time
s = " "
# ss_1
start = time.clock()
s_1 = S_1()
ans = s_1.lengthOfLongestSubstring(s)
print(ans,time.clock()-start)

# ss_2
start = time.clock()
s_2 = S_2()
ans = s_2.lengthOfLongestSubstring(s)
print(ans,time.clock()-start)



# 3236 ms	13.9 MB	python3
# 168 ms	13.4 MB	python3