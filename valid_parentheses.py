'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self,s):
        """
        Check if the brackets '()[]{}' in the string are correctly placed.

        Args:
        s (str): The string containing the brackets.

        Returns:
        bool: True if the brackets are correctly placed, False otherwise.
        """
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        open_brackets = set(bracket_map.keys())
        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack  # True if stack is empty, meaning all brackets are closed properly


sol=Solution()
print(sol.isValid("()"))