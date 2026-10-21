class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(w)) + "#" + w for w in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)   # procura o '#' já em C, sem loop Python
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res