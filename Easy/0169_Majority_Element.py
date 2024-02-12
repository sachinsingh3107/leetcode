class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1
        freq = Counter(nums)
        nu = len(nums)
        for key, value in freq.items():
            if value > (nu/2):
                return key

        # Solution 2
        nu = len(nums)
        nums.sort()
        return nums[nu//2]
