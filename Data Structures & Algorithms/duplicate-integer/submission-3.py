class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_arr = {}
        for entry in nums:
            if entry in in_arr:
                return True
            else:
                in_arr[entry] = 1
        return False
            
        