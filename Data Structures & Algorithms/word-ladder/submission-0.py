class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = []
        for word in wordList:
            if len(word) == len(beginWord):
                words.append(word)
        d = 0
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        count = 1
        while q:
            for i in range(len(q)):
                w = q.popleft()
                
                if w == endWord:
                    return count
                for word in words:
                    if word in visited:
                        continue
                    diff = 0
                    for i in range(len(w)):
                        if w[i] != word[i]:
                            diff += 1
                    if diff == 1:
                        q.append(word)
                        visited.add(word)
            count += 1
        return 0