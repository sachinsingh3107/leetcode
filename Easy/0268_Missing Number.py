class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nu_elements = len(nums)

        return int((nu_elements * ((nu_elements + 1) / 2)) - sum(nums))