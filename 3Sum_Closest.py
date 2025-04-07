"""16. 3Sum Closest
Medium
Topics
Companies
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104"""


def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest_sum





if __name__ == "__main__":
    # Test 1: nums = [-1,2,1,-4], target = 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    result1 = threeSumClosest(nums1, target1)
    print(f"Test 1: nums = {nums1}, target = {target1} -> Closest sum: {result1}")
    
    # Test 2: nums = [0, 0, 0], target = 1
    nums2 = [0, 0, 0]
    target2 = 1
    result2 = threeSumClosest(nums2, target2)
    print(f"Test 2: nums = {nums2}, target = {target2} -> Closest sum: {result2}")

    # Test 3: nums = [-10, -3, 1, 2, 4, 6, 8, 10, 12, 15], target = 20
    nums3 = [-10, -3, 1, 2, 4, 6, 8, 10, 12, 15]
    target3 = 20
    result3 = threeSumClosest(nums3, target3)
    print(f"Test 3: nums = {nums3}, target = {target3} -> Closest sum: {result3}")