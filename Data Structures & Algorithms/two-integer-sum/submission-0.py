class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_indices = {}

        for index, number in enumerate(nums):
            # checks each element we already know in the hash table
            for known_index in known_indices:
                # if the number in the list + the number in the hash table we are checking
                # is the target, then we return the index of each
                if(number + known_indices.get(known_index) == target):
                    return [known_index, index]

            known_indices[index] = number

        
        