class Solution:
    def romanToInt(self, s: str) -> int:

        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

        soma = 0
        prev = 0

        for x in s[::-1]:
            value = dict.get(x)

            if value >= prev:
                soma = soma + value
            else:
                soma = soma - value 
            
            prev = value
            
        return soma


