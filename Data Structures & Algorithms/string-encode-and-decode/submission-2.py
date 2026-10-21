class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + "#" + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        idx = 0
        strs = []
        while idx < len(s):
            hashIdx = s.index("#", idx)      # acha o '#' em C, sem loop Python
            count = int(s[idx:hashIdx])      # tamanho inteiro de uma vez
            start = hashIdx + 1
            strs.append(s[start:start + count])  # fatia a palavra inteira
            idx = start + count
        return strs