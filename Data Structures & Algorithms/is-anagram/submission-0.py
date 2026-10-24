class Solution:
    def isAnagram(self,st1,st2):
        one=sorted(st1)
        two=sorted(st2)
        if one==two :
            return True
        else:
            return False
          
        