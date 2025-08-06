class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0 
        n = len(s)

        # Iterate over all possible substrings of the string
        for i in range(n): 
            d = dict()  # Dictionary to store character frequencies in current substring

            for j in range(i, n):
                # Update frequency of the current character
                if s[j] in d:
                    d[s[j]] += 1 
                else:
                    d[s[j]] = 1 

                # Compute the beauty of the current substring
                # Beauty = max frequency - min frequency (excluding 0s)
                a = max(d.values())
                b = min(d.values())

                beauty += (a - b)  # Add beauty of this substring to total

        return beauty
