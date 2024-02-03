import pdb


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.values = {}

    def get(self, key: int) -> int:
        if self.values.get(key) is not None:
            self.count += 1
            self.cache[key] = self.count
            return self.values[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.values) == self.capacity and key not in self.values.keys():
            _del_key = min(self.cache, key=self.cache.get)
            del self.cache[_del_key]
            del self.values[_del_key]
        self.values[key] = value
        self.count += 1
        self.cache[key] = self.count


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(1, 3)
print(lru.get(2))
print(lru.get(1))
#pdb.set_trace()
#lru.put(4, 4)
#print(lru.get(1))
#print(lru.get(3))
#print(lru.get(4))
