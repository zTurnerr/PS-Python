class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            # print(target - nums[i] in nums[i+1:], target - nums[i] , nums[i+1:])
            temp = target - nums[i]
            if temp in nums[i+1:]:
                print('ssssssssssssssss')
                index1 = i
                if temp == nums[i]:
                    index2 = nums[i+1:].index(temp) + i+1
                else:
                    index2 = nums.index(temp)
                break
        return [index1, index2]



x = Solution()

print(x.twoSum([3,2,4], 6))
print('==============================')
print('==============================')
print('==============================')
print(x.twoSum([2,7,11,15], 9))
print('==============================')
print('==============================')
print('==============================')
print(x.twoSum([3,1,3], 6))

print('==============================')
print('==============================')