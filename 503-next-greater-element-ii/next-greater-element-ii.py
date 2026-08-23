class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            for j in range(1,n):
                nxt=(i+j)%n
                if nums[i]<nums[nxt]:
                    ans[i]=nums[nxt]
                    break
        return ans
        