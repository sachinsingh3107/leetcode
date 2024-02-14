class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Solution 1
        for word in words:
            start, end = 0, len(word)-1 
            palindrome = True
            while start <= end and palindrome:
                if word[start] != word[end]:
                    palindrome = False
                start += 1
                end -= 1

            if palindrome:
                return word

        # Solution 2
        for word in words:
            if word == word[::-1]:
                return word

        return ""