class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common_element = counts.most_common(k)
        result=[]
        for item in most_common_element:
            result.append(item[0])
        return result 
        