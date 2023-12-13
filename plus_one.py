'''
https://leetcode.com/problems/plus-one/description/
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_position=-1
        while (-last_position)!=len(digits)+1:
            if digits[last_position]==9:
                digits[last_position]=0
                last_position-=1
            else:
                digits[last_position]+=1
                return digits
        
        return [1,0]+digits[1:]
    

