class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        s = []

        def recurse(op, closed):
            if closed == n:
                t = ''.join(s)
                arr.append(t)
                return
            elif op == closed:
                s.append('(')
                recurse(op + 1, closed)
                s.pop()
            elif op == n:
                s.append(')')
                recurse(op, closed + 1)
                s.pop()
            else:
                s.append('(')
                recurse(op + 1, closed)
                s.pop()
                s.append(')')
                recurse(op, closed + 1)
                s.pop()


        recurse(0, 0)
        return arr

            
        
        