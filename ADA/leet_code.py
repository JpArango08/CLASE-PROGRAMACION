"""
class Solution(object):
    def combinationSum(self, candidates, target, current = [], result = [], pos= 0):
        if sum(current) == target:
            result.append(current)
            return
        elif sum(current) > target:
            return
        for i in range(pos, len(candidates)):
            self.combinationSum(candidates,target, current + [candidates[i]], result, i )
        return result
S = Solution()
candidates = [2,3,5]
target = 8
print(S.combinationSum(candidates,target))
"""
"""
class Solution(object):
    def combinationSum2(self, candidates, target, current = [], result = [], pos= 0, ready = None):
        if not ready:
            candidates.sort()
            ready= True
        if sum(current) == target:
            result.append(current)
            return 
        elif sum(current) > target:
            return
        for i in range(pos, len(candidates)):
            if i > pos and candidates[i] == candidates[i-1]:
                continue
            self.combinationSum2(candidates,target, current + [candidates[i]], result, i+1, ready)
        return result
S = Solution()
candidates = [2,5,2,1,2]
target = 5
print(S.combinationSum2(candidates,target))
"""
"""
class Solution(object):
    def permute(self, nums, current = [], permutations = []):
        if len(current) == len(nums):
            permutations.append(current)
            return
        for i in range( len(nums)):
            if nums[i] in current:
                continue
            self.permute(nums, current+[nums[i]], permutations )
        return permutations
S = Solution()
n= [0,1]
print(S.permute(n))
"""
"""
class Solution(object):

    def permuteUnique(self, nums, current=[], permutations=[], posiciones=[]):
        if len(current) == len(nums):
            permutations.append(current.copy())
            return
        nums.sort()
        for i in range(len(nums)):
            # Esta posición ya fue utilizada
            if i in posiciones:
                continue
            # Evitar generar la misma rama
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in posiciones:
                continue
            posiciones_copy = posiciones.copy()
            posiciones_copy.append(i)
            self.permuteUnique(nums,current + [nums[i]],permutations,posiciones_copy)
        return permutations
S = Solution()
n= [1,1,2]
print(S.permuteUnique(n))
"""