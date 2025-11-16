"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
Example 2:

Input: stones = [31,26,33,21,40]
Output: 5

"""



class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStoneWeight = sum(stones)
        n = len(stones)
        cache = [[None for _ in range(sumStoneWeight+1)] for _ in range(n+1)]
        return self.helper(stones,0,0,0,cache)
    def helper(self,stones,idx,sumL,sumR,cache):
        if idx==len(stones):
            return abs(sumL-sumR)
        
        if(cache[idx][sumL] is not None):
            return cache[idx][sumL]
        cache[idx][sumL] = min(self.helper(stones,idx+1,sumL+stones[idx],sumR,cache),
            self.helper(stones,idx+1,sumL,sumR+stones[idx],cache))
        return cache[idx][sumL]
    


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for s in stones:
            for j in range(target, s - 1, -1):
                dp[j] |= dp[j - s]

        for j in range(target, -1, -1):
            if dp[j]:
                return total - 2*j