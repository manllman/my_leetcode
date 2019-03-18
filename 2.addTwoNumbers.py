# !python3
# -*- coding:utf-8 -*- 
# @Author:Sqing
# @Time:2019年03月18日14:56

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 就像你在纸上计算两个数字的和那样，我们首先从最低有效位也就是列表 l1l1 和 l2l2 的表头开始相加。
# 由于每位数字都应当处于 0 \ldots 90…9 的范围内，我们计算两个数字的和时可能会出现“溢出”。
# 例如，5 + 7 = 125+7=12。
# 在这种情况下，我们会将当前位的数值设置为 22，
# 并将进位 carry = 1carry=1 带入下一次迭代。
# 进位 carrycarry 必定是 00 或 11，
# 这是因为两个数字相加（考虑到进位）可能出现的最大和为 9 + 9 + 1 = 199+9+1=19。
# class Solution:
    def addTwoNumbers(self, l1, l2):
        # 存储结果
        re = ListNode(0)
        r = re
        carry = 0  # 进位表示
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s//10
            r.next = ListNode(s%10)
            r = r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            # 如果最后有进位，也要把大于10的数分开
            r.next = ListNode(1)
        return re.next