class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = 1
        while number <= n:
            if number == n:
                return True

            number = number << 1

        return False