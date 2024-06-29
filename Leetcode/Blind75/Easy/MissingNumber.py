# Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

#solution-1 basic is the we will search whole array by making array sorted and finding element which is missing
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedlist=sorted(nums)
        for i in range(len(sortedlist)):
            if i!=sortedlist[i]:
                return i
        if len(nums)!=sortedlist[len(nums)-1]:
            return len(nums)
        return 0
        



#solution -2 we know n*n+1/2 is sum of n natural numbers and we are adding all elements in array
# if we subtract the added sum from formula value we get the number that is missing because if all are present we will get 0 since it has all elements in range n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums)*(len(nums)+1))//2 )- sum(nums)