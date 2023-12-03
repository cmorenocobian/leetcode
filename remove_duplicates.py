'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

def removeDuplicates(nums: list[int]) -> int:
    cnt=0
    for pos in range(1, len(nums)):
        if nums[cnt]!=nums[pos]:
            cnt+=1
            nums[cnt]=nums[pos]
            
    return cnt+1



print(removeDuplicates([1,1,2]))


