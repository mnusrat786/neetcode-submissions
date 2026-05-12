class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max1 = 0
        set1 = set(nums)
        for i in set1:
            if i-1 not in set1:
                length = 1
                while i+length in set1:
                    length+=1
                max1 = max(max1,length)   
        return max1     

                
        