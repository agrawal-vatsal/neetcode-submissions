class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        start, end = 0, 0
        
        # Helper function to expand around a center
        def expandAroundCenter(left: int, right: int) -> int:
            # Expand as long as pointers are in bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            # (right - left - 1) because the while loop breaks AFTER pointers step out of bounds
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
            len1 = expandAroundCenter(i, i)
            
            # Case 2: Even length palindromes (e.g., "abba", center is between 'b' and 'b')
            len2 = expandAroundCenter(i, i + 1)
            
            # Find the max length found at this center
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our global start and end bounds
            if max_len > (end - start):
                # Calculate new start and end indices based on the center i
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]