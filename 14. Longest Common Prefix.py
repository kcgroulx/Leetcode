class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # Finds the minimum length string in strs[]
        minLength = len(strs[0])
        for string in strs:
            if( len(string) < minLength ):
                minLength = len(string)

        # If all strings at index i have the same char, add it to prefix 
        # else return the current value of prefix
        for i in range(0, minLength):
            char = strs[0][i]
            for string in strs:
                if (char != string[i]):
                    return prefix
            prefix += char
            
        return prefix  