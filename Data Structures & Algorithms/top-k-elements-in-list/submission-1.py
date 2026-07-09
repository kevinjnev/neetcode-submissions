class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap, iterate through nums
        frequencies = {}
        for number in nums:
            #add 1 to the frequency of the number if there is a value, if not a key is made for that number and value is 1
            frequencies[number] = 1 + frequencies.get(number, 0)

        #sort hashmap by descending order of values and get the first k keys, those are the k most frequent numbers
        sortedfreq = sorted(frequencies, key = frequencies.get, reverse = True)
        return sortedfreq[:k]