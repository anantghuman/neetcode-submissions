class Node:
    def __init__(self, ch):
        self.ch = ch 
        self.hm = {}
        self.ends = False
class WordDictionary:

    def __init__(self):
        self.head = Node(' ')
        

    def addWord(self, word: str) -> None:
        t = self.head
        for ch in word:
            if ch in t.hm:
                t = t.hm[ch]
            else:
                t.hm[ch] = Node(ch)
                t = t.hm[ch]
        t.ends = True
        

    def search(self, word: str) -> bool:
        def search_rec(word, index, t):
            if len(word) == index:
                return t.ends
            if word[index] == '.':
                for key in t.hm.keys():
                    if search_rec(word, index + 1, t.hm[key]):
                        return True
                return False
            elif word[index] in t.hm:
                return search_rec(word, index + 1, t.hm[word[index]])
            else:
                return False

        t = self.head
        return search_rec(word, 0, t)
        
        
