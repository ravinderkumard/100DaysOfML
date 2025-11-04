"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 https://github.com/ravinderkumard/dsa-dec24-feb25/blob/main/DP/01_416.%20Partition%20Equal%20Subset%20Sum

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total%2!=0:
            return False
        
        target = total//2
        prev = [False] * (target+1)
        prev[0] = True
        for num in nums:
            for j in range(target,num-1,-1):
                prev[j] = prev[j] or prev[j-num]

        return prev[target]

        