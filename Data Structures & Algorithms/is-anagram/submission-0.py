class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = sorted(s)
        secondWord = sorted(t)
        
        if firstWord == secondWord:
            return True
        else:
            return False