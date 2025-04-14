class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups anagrams from a list of strings.
        
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary to hold sorted string as key and list of anagrams as value
        anagrams = {}

        # Loop through each string in the input list
        for s in strs:
            # Sort the string to use as a key (anagrams will have the same sorted form)
            key = ''.join(sorted(s))
            
            # If the key exists, append the original string to the list
            if key in anagrams:
                anagrams[key].append(s)
            else:
                # If the key doesn't exist, create a new list with this string
                anagrams[key] = [s]

        # Return all the grouped anagram lists
        return list(anagrams.values())


# ------------------ Testing the function ------------------

# Example input: list of strings to group as anagrams
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create an instance of the Solution class
sol = Solution()

# Call the groupAnagrams method with the input
output = sol.groupAnagrams(strs)

# Print the result
print(output)
