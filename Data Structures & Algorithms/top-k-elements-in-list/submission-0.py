class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap, iterate through nums and check if each number is already a key in the hashmap
        frequencies = {}
        for number in nums:
            #when it is, change the value for that key
            if number in frequencies:
                frequencies[number] += 1
            #whenever it is not, add a new key of that number and set its value to 1
            else:
                frequencies[number] = 1
        #sort hashmap by descending order of values and get the first k keys, those are the k most frequent numbers
        sortedfreq = sorted(frequencies, key = frequencies.get, reverse = True)
        return sortedfreq[:k]    