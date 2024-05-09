from statistics import mode 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maisRepete = mode(nums)
        qntRepete = nums.count(maisRepete)
        if qntRepete *2 >= len(nums):
            return maisRepete
        else:
            return -1
        