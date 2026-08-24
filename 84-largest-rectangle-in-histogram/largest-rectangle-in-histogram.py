class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []  # (index, height)
        n = len(heights)
        ma = 0
        
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                idx, ht = st.pop()
                ma = max(ma, ht * (i - idx))
                start = idx
            st.append((start, h))
        
        # Handle remaining stack
        for idx, ht in st:
            ma = max(ma, ht * (n - idx))
        
        return ma
