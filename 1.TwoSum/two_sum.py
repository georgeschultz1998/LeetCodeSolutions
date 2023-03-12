class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        for index2 in range(len(nums)):
            if(target - nums[index2]) in hashmap:
                return hashmap[target - nums[index2]], index2
            hashmap[nums[index2]] = i
            i+=1
