'''
https://leetcode.com/problems/search-insert-position/submissions/
'''

class Solution:
    def searchInsert0(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            while target>nums[0]:
                target=target-1
                try:
                    return nums.index(target)+1
                except:
                    pass
            return 0
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            if target < nums[0]:
                return 0
            else:
                for pos, val in enumerate(nums):
                    if val > target:
                        return pos-1
