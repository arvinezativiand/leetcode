class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return[x and y for x in range(len(nums)) for y in range(x, len(nums)) if (nums[x] + nums[y] == target)]

lst = Solution()
print(lst.twoSum([2, 7, 4, 3], 9))