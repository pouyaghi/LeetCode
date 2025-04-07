class Solution(object):
    def romanToInt(self, s):
        # Initialize the output variable
        Output = 0
        
        # Define the Roman numeral values in a dictionary
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # Loop through the Roman numeral string (except the last character)
        for i in range(len(s) - 1):
            # If the current character's value is less than the next character's value
            if romanDict[s[i]] < romanDict[s[i + 1]]:
                Output -= romanDict[s[i]]  # Subtract current value (for cases like IV or IX)
            else:
                Output += romanDict[s[i]]  # Add current value (for normal cases like VI or VII)
        
        # Add the value of the last character (it doesn't need a check against the next character)
        Output += romanDict[s[-1]]
        
        return Output


# Example 1: "III" -> 3
# Explanation: I + I + I = 3
solution = Solution()
print(solution.romanToInt("III"))  # Output: 3

# Example 2: "LVIII" -> 58
# Explanation: L = 50, V = 5, III = 3
print(solution.romanToInt("LVIII"))  # Output: 58

# Example 3: "MCMXCIV" -> 1994
# Explanation: M = 1000, CM = 900, XC = 90, IV = 4
print(solution.romanToInt("MCMXCIV"))  # Output: 1994

# Example 4: "IV" -> 4
# Explanation: IV means 5 - 1 = 4
print(solution.romanToInt("IV"))  # Output: 4

# Example 5: "IX" -> 9
# Explanation: IX means 10 - 1 = 9
print(solution.romanToInt("IX"))  # Output: 9