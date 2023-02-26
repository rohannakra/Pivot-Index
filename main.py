# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

def pivot_index(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    
    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))

# --------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
    
        return -1
