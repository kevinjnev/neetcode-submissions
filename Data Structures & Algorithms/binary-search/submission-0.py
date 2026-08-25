class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            split = left + (right - left) // 2
            if(nums[split] < target):
                left = split + 1
            elif(nums[split] > target):
                right = split - 1
            else:
                return split
        return -1

        