'''
https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt0(self, s: str) -> int:
        s=(s.replace('IV', 'IIII').replace('IX', 'VIIII')
            .replace('XL', 'XXXX').replace('XC','LXXXX')
            .replace('CD', 'CCCC').replace('CM', 'DCCCC')
            )
        conversion={'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }
        total=0
        for i in conversion.keys():
            total+= s.count(i)*conversion[i]
        return total
    
    def romanToInt(self, s: str) -> int:
        conversion={'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = conversion[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
        