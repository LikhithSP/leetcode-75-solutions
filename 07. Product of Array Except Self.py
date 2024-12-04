class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = list(accumulate(nums, operator.mul))
        sufix_mult = list(accumulate(nums[::-1], operator.mul))[::-1]

        res = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                res.append(sufix_mult[1])
            elif i == n - 1:
                res.append(prefix_mult[n-2])
            else:
                res.append(prefix_mult[i-1] * sufix_mult[i+1])
        
        return res
