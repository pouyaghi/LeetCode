class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # If the list is empty, return 0 since there are no unique elements
        if not nums:
            return 0

        # Initialize the pointer for the position of the last unique element
        i = 0

        # Loop through the list starting from the second element
        for j in range(1, len(nums)):
            # If the current element is different from the last unique one
            if nums[j] != nums[i]:
                # Move the unique pointer forward
                i += 1
                # Copy the current element to the new position
                nums[i] = nums[j]
                # This effectively overwrites duplicates and keeps only unique elements in the beginning of the list

        # Return the count of unique elements (index + 1 because index starts from 0)
        return i + 1
