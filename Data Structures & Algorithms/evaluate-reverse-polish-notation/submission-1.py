class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s in '+-*/':
                num2 = st.pop()
                num1 = st.pop()
                if s == '+':
                    st.append(num1 + num2)
                if s == '-':
                    st.append(num1 - num2)
                if s == '*':
                    st.append(num1 * num2)
                if s == '/':
                    st.append(int(num1 / num2))  
            else:
                st.append(int(s))
        return st[0]

        