'''
https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome0(self, x: int) -> bool:
        if (x>=0) and (str(x)==str(x)[::-1]):
            return True
        else:
            return False

    def isPalindrome(self, x: int) -> bool:

        return str(x)==str(x)[::-1]
    


