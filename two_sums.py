'''
https://leetcode.com/problems/two-sum/

'''

class Solution:
    # 67 ms
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length=len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if (nums[i] + nums[j]==target):
                    return [i,j]
    #71 ms
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for pos1, i in enumerate(nums):
            for pos2, j in enumerate(nums[pos1+1:]):
                if (i+j==target):
                    return [pos1,pos1+1+pos2]
    #71 ms
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        for pos, i in enumerate(nums):
            compl= target-i
            if compl in nums[pos+1:]:
                return [pos,nums.index(compl, pos+1, len(nums))]
            