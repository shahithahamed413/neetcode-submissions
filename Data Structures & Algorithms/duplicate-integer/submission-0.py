class Solution:
    def hasDuplicate(self, num):
        check = set()
        for i in num:
            if i in check:
                return True
            check.add(i)
        return False