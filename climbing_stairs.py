class Solution:
    def climbStairs(self, n: int) -> int:


        # DYNAMIC PROGRAMMING
        dp = [0] * (n+1)
        dp[-1],dp[-2] = 1,1
        print(dp)

        for i in range(n-2,-1,-1):
            dp[i] = dp[i+1] + dp[i+2]
            

        return dp[0]
        

        

        