from sortedcontainers import SortedList
class MinStack:

    def __init__(self):
        self.arr = []
        self.l = SortedList()

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.l.add(val)

    def pop(self) -> None:
        self.l.remove(self.arr.pop())

    def top(self) -> int:
        return self.arr[len(self.arr) - 1]

    def getMin(self) -> int:
        return self.l[0]
        
