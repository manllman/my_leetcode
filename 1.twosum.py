# !python3
# -*- coding:utf-8 -*- 
# @Author:Sqing
'''
s3 > s4 > s2 > s1
'''
import time
nums = [3,3]
target = 6
# sqing的小年轻的算法
class S1_sqing:
    def twoSum(self, nums, target):
        # 挨个问
        for j in range(len(nums)-1):
            sub_num = target-nums[j]
            for k in range(j+1,len(nums)):
                if nums[k] == sub_num:
                    return [j,k]


class S2_morty:
    def twoSum(selfself,nums,target):
        '''
        首尾递进排序
        :param nums List[int]:
        :param target int:
        :return List[int]:
        '''
        sorted_id = sorted(range(len(nums)),key=lambda k:nums[k])
        head = 0
        tail = len(nums) -1
        sum_result = nums[sorted_id[head]]+nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -=1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]]+nums[sorted_id[tail]]
        return [sorted_id[head],sorted_id[tail]]

class S3_morty2():
    def twoSum(self,nums,target):
        '''
        使用字典
        :param nums:
        :param target:
        :return:
        '''
        hashmap = {}
        for index,num in enumerate(nums):
            sub_num = target-num
            if sub_num in hashmap:
                return [hashmap[sub_num],index]
            hashmap[num] = index
        return None


class S4_nobody(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            nums_copy=nums[:]
            diff=target-nums_copy.pop(i)
            #比s3多了一次遍历
            if diff in nums_copy:
                returnList=[i,nums_copy.index(diff)+1]
                return returnList


# s1测试
start = time.clock()
s1 = S1_sqing()
print(s1.twoSum(nums,target),time.clock()-start)
# 1.0674268935742543e-05

#s2测试
start = time.clock()
s2 = S2_morty()
print(s2.twoSum(nums,target),time.clock()-start)
# 9.032073714859077e-06

#s3测试
start = time.clock()
s3 = S3_morty2()
print(s3.twoSum(nums,target),time.clock()-start)
# 3.6949392469878118e-06

#s4测试
start = time.clock()
s4 = S4_nobody()
print(s4.twoSum(nums,target),time.clock()-start)
# 4.105488052208675e-06