# ============================================================
# Category 9: Design Problems
# Core pattern: combine multiple data structures for O(1) ops
# ============================================================

from collections import OrderedDict, defaultdict

# O(1) time for all operations, O(capacity) space
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest = self.order.popitem(last=False)
                del self.cache[oldest[0]]
            self.cache[key] = value
            self.order[key] = True

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print("LRUCache.get(1):", lru.get(1))
lru.put(3, 3)
print("LRUCache.get(2) after eviction:", lru.get(2))


# O(1) time for all operations, O(n) space
class MinStack:
    def __init__(self):
        self.main = []
        self.min_stack = []

    def push(self, value):
        self.main.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.main.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.main[-1]

    def get_min(self):
        return self.min_stack[-1]

ms = MinStack()
for v in [3, 1, 4, 1, 5]:
    ms.push(v)
print("MinStack.get_min():", ms.get_min())
print("MinStack.top():", ms.top())


# O(1) get/put amortized, O(k) space (k = distinct frequencies)
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_value = {}
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_value:
            return -1
        self._bump_freq(key)
        return self.key_value[key]

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key_value:
            self.key_value[key] = value
            self._bump_freq(key)
            return
        if len(self.key_value) >= self.capacity:
            evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_value[evict_key]
            del self.key_freq[evict_key]
        self.key_value[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1][key] = True
        self.min_freq = 1

    def _bump_freq(self, key):
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        new_freq = freq + 1
        self.key_freq[key] = new_freq
        self.freq_keys[new_freq][key] = True

lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print("LFUCache.get(1):", lfu.get(1))
lfu.put(3, 3)
print("LFUCache.get(2) (evicted):", lfu.get(2))


# O(1) average case, O(n) space
class RandomizedSet:
    def __init__(self):
        self.elements = []
        self.index_map = {}

    def insert(self, value):
        if value in self.index_map:
            return False
        self.index_map[value] = len(self.elements)
        self.elements.append(value)
        return True

    def remove(self, value):
        if value not in self.index_map:
            return False
        idx = self.index_map[value]
        last = self.elements[-1]
        self.elements[idx] = last
        self.index_map[last] = idx
        self.elements.pop()
        del self.index_map[value]
        return True

    def get_random(self):
        import random
        return self.elements[random.randint(0, len(self.elements) - 1)]

rs = RandomizedSet()
print("RandomizedSet.insert(1):", rs.insert(1))
print("RandomizedSet.insert(2):", rs.insert(2))
print("RandomizedSet.get_random() (1 or 2):", rs.get_random())


# O(1) average case for all ops, O(n) space
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

uf = UnionFind(5)
print("UnionFind.union(0, 1):", uf.union(0, 1))
print("UnionFind.union(1, 2):", uf.union(1, 2))
print("UnionFind.find(0) == find(2):", uf.find(0) == uf.find(2))


# O(log n) average for all ops, O(n) space
class MedianFinder:
    def __init__(self):
        import heapq
        self.small = []  # max heap (negate values)
        self.large = []  # min heap
        self.small_size = 0
        self.large_size = 0

    def addNum(self, num):
        import heapq
        if self.small_size == self.large_size:
            if self.large and num > self.large[0]:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            if num < -self.small[0]:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
            self.large_size += 1

    def findMedian(self):
        if self.small_size > self.large_size:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

mf = MedianFinder()
for num in [1, 2]:
    mf.addNum(num)
print("MedianFinder median after [1, 2]:", mf.findMedian())


# O(1) average case, O(capacity) space  [MIXED: design + multiset logic]
class TimeBasedKeyValueStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        values = self.store[key]
        lo, hi = 0, len(values) - 1
        result = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result

tbkv = TimeBasedKeyValueStore()
tbkv.set("foo", "bar", 1)
tbkv.set("foo", "bar2", 3)
print("TimeBasedKeyValueStore.get('foo', 2):", tbkv.get("foo", 2))
print("TimeBasedKeyValueStore.get('foo', 4):", tbkv.get("foo", 4))
