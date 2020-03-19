
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

from typing import List
class Solution:
    '''
        Returns indices such that the sum of two elements of
        nums is equal to target.
    '''
    def twoSum(self, nums : List[int], target : int) -> List[int]:
        numset = set(nums)
        for i, x in enumerate(nums):
            to_search = target - x
            if to_search in numset:
                found = nums.index(to_search)
                if found != i :
                    return [i, found]
        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Recherche de couple a, b tel que a + b = -c
        '''
        res = []
        n = len(nums)
        for i, target in enumerate(nums):
            for j in range(n) :
                if i < j :
                    to_search = - target - nums[j]
                    if to_search in set(nums[j + 1:]) :
                        found = nums.index(to_search, j + 1)
                        if found != j and found != i :
                            values = sorted([target, nums[j], nums[found]])
                            if values not in res :
                                res.append(values)
        return res

if __name__ == "__main__":
    S = Solution()
    x = S.twoSum([2, 7, 11, 15], 9)
    y = S.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    print(y)
    y = S.threeSum([0,0,0])
    print(y)