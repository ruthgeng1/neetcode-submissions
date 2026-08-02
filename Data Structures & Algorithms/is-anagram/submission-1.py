class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            sum_of_s = 0
            sum_of_t = 0

            for char in s:
                sum_of_s += ord(char) ** 2
            for char in t:
                sum_of_t += ord(char) ** 2
            
            return sum_of_s == sum_of_t
