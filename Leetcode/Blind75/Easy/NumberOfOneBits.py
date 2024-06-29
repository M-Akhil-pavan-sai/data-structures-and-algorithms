# 191. Number of 1 Bits
# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits
#  it has (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

# Constraints:

# 1 <= n <= 231 - 1
 

# Follow up: If this function is called many times, how would you optimize it?

# solution-1: using basic method intuition convert to binary and count number of 1 in the binary string it is O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n))[2:].count('1')
    
    
# solution-2 using bit wise & operator to find what is the last bit of the number if 1 then increment the counter so time complexity will be checking 32 positions in the number
# to check each position we are right shifting the elements that we have 32 times. time complexity is O(32) which is constant time
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for i in range(32):
            if n>>i & 1:
                count+=1
        return count
