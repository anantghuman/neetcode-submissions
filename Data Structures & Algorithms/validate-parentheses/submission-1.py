class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == ')':
                if len(st) == 0 or st.pop() != '(':
                    return False
            elif ch == '}':
                if len(st) == 0 or st.pop() != '{':
                    return False
            elif ch == ']':
                if len(st) == 0 or st.pop() != '[':
                    return False
            else:
                st.append(ch)
        return len(st) == 0
        