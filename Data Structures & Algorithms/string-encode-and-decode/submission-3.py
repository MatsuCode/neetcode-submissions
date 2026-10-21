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
            hashIdx = s.index("#", idx)
            count = int(s[idx:hashIdx])
            start = hashIdx + 1
            strs.append(s[start:start + count])
            idx = start + count
        return strs