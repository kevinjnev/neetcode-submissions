class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_arr = set()
        for entry in nums:
            if entry in in_arr:
                return True
            else:
                in_arr.add(entry)
        return False
            
        