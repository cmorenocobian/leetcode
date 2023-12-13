'''
https://leetcode.com/problems/add-binary/
'''

a= "100101"
b="111110011"
class Solution:
    def addBinary0(self, a: str, b: str) -> str:
        first, second = (a,b) if len(a)>=len(b) else (b,a)
        second=second.zfill(len(first))
        first,second=first[::-1], second[::-1]

        final=""
        carry=0
        for val1, val2 in zip(first,second):
            suma=int(val1) + int(val2)+carry
            if suma<2:
                final+= str(suma)
                carry=0
            elif suma==2:
                final += '0'
                carry=1
            else:
                final += '1'
                carry=1
            print(f"{val1}+{val2}={suma};{final}")
        if carry:
            final+='1'
        print(f"Resultado: {final[::-1]}")
        return final[::-1]
    
    def addBinary(self, a: str, b: str) -> str:
        # Hago que a sea siempre la cadena más larga
        if len(b) > len(a):
            a, b = b, a

        # completo b con 0s
        b = b.zfill(len(a))

        result = []
        carry = 0

        # Recorro las cadenas en orden inverso para poder sumarlas
        for val1, val2 in zip(a[::-1], b[::-1]):
            total = int(val1) + int(val2) + carry
            result.append(str(total % 2))
            carry = total // 2

        # Si al terminar carry no es cero añado un 1
        if carry:
            result.append('1')

        # cambio el orden
        return ''.join(result[::-1])