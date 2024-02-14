class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        index = 0
        res = []
        while index < len(pos):
            res.append(pos[index])
            res.append(neg[index])
            index += 1

        return res
        