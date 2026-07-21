class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        missing_count = len(t)
        best_left = 0
        min_length = float('inf')
        left =0

        for right, char in enumerate (s):
            if needed[char]>0:
                missing_count -=1
            needed[char]-=1

            while missing_count == 0:
                current_len = right - left + 1
                if current_len < min_length:
                    min_length = current_len
                    best_left = left

                needed[s[left]] +=1
                if needed[s[left]] > 0:
                    missing_count +=1
                left +=1

        if min_length == float('inf'):
            return ""
        return s[best_left : best_left +min_length]

        