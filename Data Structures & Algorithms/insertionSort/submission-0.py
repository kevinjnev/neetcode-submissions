# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        sorted = []

        #the index i will iterate through the whole array, which means we will be sorting one element at a time
        #into the part of the array that comes before it, which should already be sorted
        for i in range(n):
            #j is used to iterate back down from i to the beginning of the array, comparing and swapping values
            #as needed
            j = i - 1

            #while the key at index j is bigger than the next key, swaps their place
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            #this adds the intermediate steps to the final output, that way 
            #you are able to see the insertion sort being performed
            sorted.append(pairs[:])

        return sorted