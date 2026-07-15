class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #can calculate the product of all the elements behind and in front of each element and multiply those together
        #to get the product of everything but that element

        #make the output array, set output[0] equal to 1
        output = [0] * len(nums)
        output[0] = 1
        #go through array once with a variable prefix starting at value 1
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            #for each element, store the prefix value in the output array, and create the next prefix by
            #multiplying this element of nums with the prefix and storing it
            output[i] = prefix
            prefix = nums[i] * prefix

        #iterate again
        for i in range(len(nums) - 1, -1, -1):
            #for each element in output multiply that element with the suffix 
             #(this is multiplying the prefix and suffix, creating the final values)
            output[i] = output[i] * suffix
            
            #multiply the suffix with the value in element i of nums and store in suffix
            suffix = nums[i] * suffix

        return output