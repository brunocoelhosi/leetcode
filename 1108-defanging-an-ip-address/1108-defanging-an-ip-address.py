class Solution:
    def defangIPaddr(self, str) -> str:
        return str.replace(".","[.]")