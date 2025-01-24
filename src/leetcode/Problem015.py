
'''
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
    Given an array nums of n integers, are there elements a, b, c in nums
    such that a + b + c = 0 ? 
    Find all unique triplets in the array which gives the sum of zero.

'''

from typing import List, Set, Tuple
class Solution:
    '''
        Returns indices such that the sum of two elements of
        nums is equal to target.
    '''
    # def twoSum(self, nums, target, ans):
    #     d = {}
    #     for i, x in enumerate(nums):
    #         if target - x in d :
    #             ans.add((x, target - x, -target))
    #         d[x] = i

    # def threeSum(self, nums: List[int]) :
    #     '''
    #         Recherche de couple a, b tel que a + b = -c
    #     '''
    #     ans : Set[Tuple[int]]= set()
    #     nums.sort()
    #     for i, y in enumerate(nums) :
    #         self.twoSum(nums, -y, ans)
    #     return ans
                
    def threeSum(self, nums: List[int]) -> List[Tuple[int]]:
        nums.sort()
        ans : Set[Tuple[int]]= set()
        for i,v in enumerate(nums):
            self.twoSum(nums[i+1:],-v,ans)
        return list(ans)

    def twoSum(self,nums,target,ans):
        d = {}
        for i,v in enumerate(nums):
            if target-v in d:
                ans.add((v,target-v,-target)) #3sum wants the numbers, while 2sum wanted the indices
            d[v] = i

from typing import Set
if __name__ == "__main__":
    S = Solution()
    A : Set[List[int]] = set()
    # x = S.twoSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], 4)
    y = S.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    print(y)