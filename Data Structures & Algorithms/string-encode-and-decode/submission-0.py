class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""

        for s in strs:
            n = len(s)
            encode += f"{n}#{s}"
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            string = s[j+1:j+1+length]
            decode.append(string)
            i = j + 1 + length
        return decode
