class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicatesList = {}
        for num in nums:
            if num in duplicatesList:
                return True
            duplicatesList[num] = ""
        return False
        