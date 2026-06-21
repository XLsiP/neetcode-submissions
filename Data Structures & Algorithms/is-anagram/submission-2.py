class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first check if same length
        #make it 2 dicts
        #if same length perform a for loop to get each value of each key
        if len(s) != len(t):
            return False
            char_S, char_T = {}, {}
            for i in range(len(s)):
                char_S[s[i]] = char_S.get(s[i], 0) + 1
                char_T[t[i]] = char_T.get(t[i], 0) + 1
            return char_S == char_T
