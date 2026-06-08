class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_indices = {}

        for index, number in enumerate(nums):
            difference = target - number
        
            if difference in known_indices:
                known_index = known_indices[difference]
                return [known_index, index]
                
            known_indices[number] = index


        
        