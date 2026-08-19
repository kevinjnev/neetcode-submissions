class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        #sort array to use two pointer algorithm on it
        nums.sort()

        for index, number in enumerate(nums):
            #this makes it so duplicates aren't used for the first number, it skips
            #the iteration if it is a dupe (sorted so it would always be just the last number)
            if index > 0 and number == nums[index - 1]:
                continue
            
            #basically two sum when looking for the other two numbers, since it is sorted
            #i use a left and right pointer to close in on any potential pairs
            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = number + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([number, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
