class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0 , len(numbers)):
            for j in range (i+1 , len(numbers)):
                if (numbers[i]+ numbers[j] == target):
                    number = [numbers[i] , numbers[j]]
                    return number 