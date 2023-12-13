'''
https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos=m+n
        while pos and n:
            pos-=1
            print(nums1[m-1], nums2[n-1], pos)
                
            if (nums1[m-1] > nums2[n-1]) and (m):
                nums1[pos]=nums1[m-1]
                m-=1
            else:
                nums1[pos]=nums2[n-1]
                n-=1
                            










'''
if m==0:
    nums1=nums2
else:
    pos=m+n
    for val1 in nums1[:m][::-1]:
        cnt=0
        for val2 in nums2[::-1]:
            pos-=1
            print(val1, val2, pos)
            
            if val1 > val2:
                nums1[pos]=val1
                break
            else:
                nums1[pos]=val2
                cnt+=1
        nums2=nums2[:-cnt]
print("Final", nums1)
'''


