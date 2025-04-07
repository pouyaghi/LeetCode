"""35. Search Insert Position
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104 """


class Solution(object):
    def searchInsert(self, nums, target):
        # Start with the full range of the list
        left, right = 0, len(nums) - 1

        # Keep searching while the range is valid
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # Case 1: target is found at mid
            if nums[mid] == target:
                return mid

            # Case 2: target is greater — search the right half
            elif nums[mid] < target:
                left = mid + 1

            # Case 3: target is smaller — search the left half
            else:
                right = mid - 1

        # If the target is not found, left is the correct insert position
        return left



"""
Explanation:
This solution uses Binary Search, which reduces the time complexity to O(log n).
Since the input list `nums` is sorted, we can efficiently cut the search range
in half each time using the `left`, `right`, and `mid` pointers.

Binary Search works by comparing the middle element to the target:
- If equal, return the index.
- If the target is greater, we move to the right half.
- If it's smaller, we move to the left half.
If the target is not found, the `left` pointer ends up at the correct insertion index.

This is much faster than a linear search, especially on large input sizes.

----------------------------------------------------------

Below is the older version of the code that also works correctly but is less efficient:

    class Solution(object):
        def searchInsert(self, nums, target):
            check = False
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                    check = True
            if check != True:
                for i in range(len(nums)):
                    if nums[i] > target:
                        return i
                        break
                    if nums[-1] < target:
                        return len(nums)

This version uses two separate `for` loops to find the target or its insert position.
Each loop goes through the list linearly, resulting in a time complexity of O(n).
While functionally correct, it's less efficient for large lists compared to the binary search version.
"""


# ----------------------------------------------------------
# Note: Time Complexity Cheat Sheet
# - O(1): Constant time (e.g., accessing an element by index)
# - O(log n): Binary search (halve the input each time)
# - O(n): Linear search or single loop through input
# - O(n log n): Efficient sorting algorithms (e.g., mergesort, heapsort)
# - O(n^2): Nested loops over the input (e.g., bubble sort)
# - O(2^n), O(n!): Exponential / factorial time (e.g., recursion-heavy problems)
# Remember: lower complexity = faster on large inputs
