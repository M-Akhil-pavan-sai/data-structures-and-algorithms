# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# solution O(n) time complexity
class Solution:
    def isValid(self, s: str) -> bool:
        d1 ={'(':1,'{':2,'[':3}
        d2={')':1,'}':2,']':3}
        final=[]
        for i in range(len(s)):
            if s[i] in d2:
                if len(final)<=0 or d1[final[len(final)-1]]!=d2[s[i]]:
                    return False
                final.pop()
            else:
                final.append(s[i])
        if len(final)==0:
            return True
        return False