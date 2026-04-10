class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.list = Node(-1)
        self.list.prev = self.list
        self.list.next = self.list


    def get(self, key: int) -> int:
        val = self.hm[key] if key in self.hm else -1
        if val != -1:
            print(val)
            self.put(key, self.hm[key])
        return val
        
        

    def put(self, key: int, value: int) -> None:
        def find_and_remove(key):
            n = self.list
            while n.next is not self.list and n.next.val != key:
                n = n.next
            if n.next is self.list:
                return False
            n.next = n.next.next
            n.next.prev = n
            return True

        if key in self.hm:
            print(key)
            find_and_remove(key)
            # adds it back in
            n = Node(key)
            n.prev = self.list
            n.next = self.list.next
            n.next.prev = n
            self.list.next = n
            self.hm[key] = value
            return

        if len(self.hm) == self.capacity:
            n = Node(key)
            print(self.list.prev.val, key)
            del self.hm[self.list.prev.val]
            self.list.prev.prev.next = self.list
            # remove end
            self.list.prev = self.list.prev.prev
            # add to front
            n = Node(key)
            n.next = self.list.next
            n.prev = self.list
            n.next.prev = n
            self.list.next = n
            self.hm[key] = value
            return
        # add to front
        self.hm[key] = value
        n = Node(key)
        n.next = self.list.next
        n.prev = self.list
        self.list.next = n
        n.next.prev = n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)