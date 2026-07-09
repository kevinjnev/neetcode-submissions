class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need to have a hashmap to store the count of each number
        count = {}
        #have an array where the indices are the count, and each count has an array for the
        #numbers that have that count, so the size is the size of list nums
        frequency = [[] for i in range(len(nums) + 1)]

        #get the counts of each number
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        #store each key in the corresponding array for its count in frequency (use count as index)
        for n, c in count.items():
            frequency[c].append(n)

        #make the results list and go through the frequency array backwards, adding the numbers stored in each index
        #until the results list is the size of k
        #at that point the results are the k most frequent numbers
        results = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                results.append(n)
                if len(results) == k:
                    return results
            