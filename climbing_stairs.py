'''
https://leetcode.com/problems/climbing-stairs
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            # Sólo se puede subir de una forma
            return 1
        elif n == 2:
            # Sólo se puede subir de 2 formas (los dos escalones de una vez o de escalón en escalón)
            return 2
        
        # Voy a crear una lista para guardar los datos y reducir el costo de cálculo
        steps=[0,1,2] + [0]*(n-2)

        # Itero para ir calculando el número de casos
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[n]



