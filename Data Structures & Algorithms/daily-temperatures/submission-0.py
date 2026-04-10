class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        st = []
        for i in range(0, len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                val, index = st.pop()
                result[index] = i - index
            st.append((temperatures[i], i))
        return result