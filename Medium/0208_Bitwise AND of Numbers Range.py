class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right or left == 0:
            return left
        
        shifts = 0
        while left != right:
            right = right >> 1
            left = left >> 1
            shifts += 1

        return left << shifts