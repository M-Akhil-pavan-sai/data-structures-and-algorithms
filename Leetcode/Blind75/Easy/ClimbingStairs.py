# 70. Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

#solution -1  using recursion base cases are either we take one step or 2 steps and recurse if more than 3 stairs are present here time limit will exceed so we can use memoization technique to store 
# values that are already computed and use them directly
class Solution:
    def fun(self,n,matrix):
        if n<=len(matrix):
            return matrix[n-1]
        if n>2:
            matrix.append(self.fun(n-1,matrix) + self.fun(n-2,matrix))
            return matrix[len(matrix)-1]

    def climbStairs(self, n: int) -> int:
        return self.fun(n,[1,2])
        
        
        
# solution - 2 using memoization but in simpler fashion
class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,2]
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(n-2):
            l.append(l[len(l)-1]+l[len(l)-2])
        return l[len(l)-1]
        
        
# solution-3 without using memory just using two variables
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        first,second=1,2
        for i in range(3,n+1):
            temp=second
            second=second+first
            first=temp
        return second