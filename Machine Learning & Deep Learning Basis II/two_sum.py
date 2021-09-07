class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

sol = Solution()
nums = [3,2,4]
target = 6
i, j = sol.twoSum(nums, target)
print('i:', i, 'j:', j)
