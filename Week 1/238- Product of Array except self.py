class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefProduct = [1] * n
        suffProduct = [1] * n
        res = [0] * n

        for i in range(1, n):
            prefProduct[i] = nums[i - 1] * prefProduct[i - 1]

        for j in range(n - 2, -1, -1):
            suffProduct[j] = nums[j + 1] * suffProduct[j + 1]

        for i in range(n):
            res[i] = prefProduct[i] * suffProduct[i]

        return res