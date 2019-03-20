# !python3
# -*- coding:utf-8 -*- 
# @Author:Sqing
# @Time:2019年03月20日20:11
# TODO：
#  给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#  并且要求算法的时间复杂度为 O(log(m + n))。
#  你可以假设 nums1 和 nums2 不会同时为空。
# ~~~~~~~~~~~~~~~~~~~~~~~

class S_1:
    def findMedianSortedArrays(self, nums1, nums2):
        sorted_nums = sorted(nums1+nums2)
        len_nums = len(sorted_nums)
        if len_nums%2 == 0 :
            mid = len_nums//2
            return (sorted_nums[mid-1]+sorted_nums[mid])/2
        return sorted_nums[len_nums//2]






#还是实现不了log2(m+n)的时间复杂度啊


import time
1,2,3,3,4,4,7
nums1 = [1, 2,3,4,7]
nums2 = [3, 4]
start = time.clock()
s_1 = S_1()
ans = s_1.findMedianSortedArrays(nums1,nums2)
print(ans,time.clock()-start)
