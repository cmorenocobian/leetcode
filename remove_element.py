'''
https://leetcode.com/problems/remove-element/
'''

class Solution:
    def removeElement0(self, nums: List[int], val: int) -> int:
        cnt=0
        for pos in range(len(nums)):
            if nums[pos] != val:

                nums[cnt]=nums[pos]
                cnt+=1
        return cnt

    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        for num in nums:
            if num != val:
                nums[cnt]=num
                cnt+=1
        return cnt  