"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? """


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]  # Input list of integers
        :type target: int  # Target sum we're looking for
        :rtype: List[int]  # Indices of the two numbers that add up to the target
        """
        # Create a hashmap (dictionary) to store the value and its index
        hashmap = {}  # key: number, value: index
        
        # Iterate over the numbers in the list (nums)
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement (what we need to add to num to reach target)
            
            # Check if the complement is already in the hashmap
            if complement in hashmap:
                # If found, return the index of the complement and the current index
                return [hashmap[complement], i]
            
            # Otherwise, add the current number and its index to the hashmap
            hashmap[num] = i
        
        # If no solution is found (although the problem guarantees one), return an empty list
        return []

# Example usage:

# Create an instance of the Solution class
solution = Solution()

# Example 1: nums = [2, 7, 11, 15], target = 9
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = solution.twoSum(nums1, target1)
print(f"Output for Example 1: {result1}")  # Output: [0, 1]

# Example 2: nums = [3, 2, 4], target = 6
nums2 = [3, 2, 4]
target2 = 6
result2 = solution.twoSum(nums2, target2)
print(f"Output for Example 2: {result2}")  # Output: [1, 2]

# Example 3: nums = [3, 3], target = 6
nums3 = [3, 3]
target3 = 6
result3 = solution.twoSum(nums3, target3)
print(f"Output for Example 3: {result3}")  # Output: [0, 1]




""" Brute Force: O(n²) — requires two nested loops to check all pairs.

Optimized Approach (with hashmap): O(n) — only requires one pass through the array, with constant-time operations for each element (lookup and insert in hashmap).

This solution is a significant improvement, reducing the complexity from quadratic time (O(n²)) to linear time (O(n))."""