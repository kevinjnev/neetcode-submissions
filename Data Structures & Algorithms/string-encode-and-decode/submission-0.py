class Solution:

    def encode(self, strs: List[str]) -> str:
        #to encode the strings i can store them as "length/string", that way when decoding
        #all you need to do is read the length until you reach a / then read the correct number of characters
        #until you reach the next encoded string
        full_encode = ""
        for string in strs:
            encoded_str = "" + str(len(string)) + "/" + string
            full_encode += encoded_str
        return full_encode

    def decode(self, s: str) -> List[str]:
        full_decode = []
        while(s != ""):
            strlen, s = s.split('/', 1)
            single = s[:int(strlen)]
            s = s[int(strlen):]
            full_decode.append(single)
        return full_decode

            


