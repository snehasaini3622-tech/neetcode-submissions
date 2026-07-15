class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_result = 0
        ptr1 = 0
        ptr2 = len(height)-1

        while (ptr1<ptr2):
            ptr = min(height[ptr1] , height[ptr2])
            result = ptr * (ptr2 - ptr1)
            max_result = max(max_result , result)

            if (height[ptr1] <= height[ptr2]):
                ptr1 += 1
            else:
                ptr2 -=1

        return max_result

