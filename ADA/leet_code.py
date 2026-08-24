class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i, n in enumerate(nums):
            if i+1 >= len(nums):
                break
            if n + nums[i+1] == target:
                result = [i, i+1]
        return result

r = [0,1,2]
c = Solution()
print(c.twoSum(r,3))
        
        
