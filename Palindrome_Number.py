"""9. Palindrome Number
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Step 2: Numbers ending with 0 (except 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        while x > reversed_half:
            # Step 3: Reverse the second half of the number
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 4: If the number is a palindrome, the two halves should be equal
        # For odd-length numbers, we can ignore the middle digit by checking x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Test cases
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))   # Output: False
