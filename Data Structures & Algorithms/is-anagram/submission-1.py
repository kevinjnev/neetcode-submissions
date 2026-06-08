class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(s)):
            return False
        # create a hashmap with each letter being a key, go through s and t, for each letter in s
        # add +1 to that key's value, for each in r -1 to that key's value, at the end if any of them are not 0 it is not an anagram
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        for char in t:
            letters[char] = letters.get(char, 0) - 1
        for letter in letters:
            if(letters[letter] != 0):
                return False
        return True
