class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        #guaranteed one correct pair by the question so while True is fine,
        #will always return
        while True:
            sum = numbers[left] + numbers[right]
            #since it is sorted we can decrease the sum by decrementing the right,
            #or increase by incrementing the left pointer, so it will find the 
            #answer by closing in on it like that
            if(sum < target):
                left += 1
            elif(sum > target):
                right -= 1
            else:
                #these indices do not start from zero so need to do + 1
                return [left + 1, right + 1]