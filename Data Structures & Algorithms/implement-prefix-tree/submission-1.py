class Node:
    def __init__(self, ch):
        self.hm = {}
        self.ch = ch
        self.end = False
    # def get(ch):
    #     return self.hm[ch]
    # def add(ch):
    #     self.hm[ch] = Node()

class PrefixTree:

    def __init__(self):
        self.head = Node(' ')
        

    def insert(self, word: str) -> None:
        t = self.head
        for ch in word:
            if ch in t.hm:
                t = t.hm[ch]
            else:
                t.hm[ch] = Node(ch)
                t = t.hm[ch]
        t.end = True


    def search(self, word: str) -> bool:
        t = self.head
        for ch in word:
            if ch not in t.hm:
                return False
            t = t.hm[ch]
        return t.end
        

    def startsWith(self, prefix: str) -> bool:
        t = self.head
        for ch in prefix:
            if ch not in t.hm:
                return False
            t = t.hm[ch]
        return True        