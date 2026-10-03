# ============================================================
# Category 9: Design — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: Combine multiple data structures for O(1) ops
# Key: Choose structures that enable fast access/update
# ============================================================

from collections import defaultdict, deque
import heapq

# ============================================================
# PROBLEM 1: LRU CACHE
# ============================================================
# What it solves: Cache with limited size, evict least recently used
# Structures: HashMap (O(1) access) + DoublyLinkedList (O(1) reorder)
# Operations: get O(1), put O(1)
# Interview angle: LFU? Time-based expiry? Multiple caches?

# BASE: LRU Cache
class LRUCache:
    """Base: Least Recently Used cache with max size"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key):
        """Get value, mark as recently used"""
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        """Put key-value, evict LRU if full"""
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.order.popleft()
            del self.cache[lru]
        self.cache[key] = value
        self.order.append(key)

# VARIANT 1A: LFU Cache (Least Frequently Used)
class LFUCache:
    """Variant A: Least Frequently Used cache"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(int)
        self.min_freq = 0
        self.freq_to_keys = defaultdict(deque)

    def get(self, key):
        """Get value, increase frequency"""
        if key not in self.cache:
            return -1
        self.freq[key] += 1
        old_freq = self.freq[key] - 1
        self.freq_to_keys[old_freq].remove(key)
        if not self.freq_to_keys[old_freq] and old_freq == self.min_freq:
            self.min_freq += 1
        self.freq_to_keys[self.freq[key]].append(key)
        return self.cache[key]

    def put(self, key, value):
        """Put key-value, evict LFU if full"""
        if self.capacity <= 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        if len(self.cache) == self.capacity:
            lfu = self.freq_to_keys[self.min_freq].popleft()
            del self.cache[lfu]
            del self.freq[lfu]
        self.cache[key] = value
        self.freq[key] = 1
        self.min_freq = 1
        self.freq_to_keys[1].append(key)

# VARIANT 1B: Time-based expiry (TTL)
class TTLCache:
    """Variant B: cache with time-to-live expiration"""
    def __init__(self, capacity, ttl_seconds):
        self.capacity = capacity
        self.ttl = ttl_seconds
        self.cache = {}
        self.expiry_time = {}
        self.order = deque()

    def get(self, key, current_time):
        """Get if not expired"""
        if key not in self.cache or self.expiry_time[key] < current_time:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value, current_time):
        """Put with TTL"""
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.order.popleft()
            del self.cache[lru]
        self.cache[key] = value
        self.expiry_time[key] = current_time + self.ttl
        self.order.append(key)

# VARIANT 1C: Multi-tier cache (L1 hot, L2 warm)
class MultiTierCache:
    """Variant C: multiple cache tiers (hot vs warm)"""
    def __init__(self, l1_capacity, l2_capacity):
        self.l1 = {}
        self.l2 = {}
        self.l1_cap = l1_capacity
        self.l2_cap = l2_capacity
        self.l1_order = deque()
        self.l2_order = deque()

    def get(self, key):
        """Get from L1 (hot), move to front"""
        if key in self.l1:
            self.l1_order.remove(key)
            self.l1_order.append(key)
            return self.l1[key]
        elif key in self.l2:
            self.l2_order.remove(key)
            self.l2_order.append(key)
            # Move to L1
            if len(self.l1) == self.l1_cap:
                evicted = self.l1_order.popleft()
                self.l2[evicted] = self.l1[evicted]
                self.l2_order.append(evicted)
            self.l1[key] = self.l2[key]
            del self.l2[key]
            self.l1_order.append(key)
            return self.l1[key]
        return -1

    def put(self, key, value):
        """Put in L1"""
        if key in self.l1:
            self.l1[key] = value
            self.l1_order.remove(key)
            self.l1_order.append(key)
        else:
            if len(self.l1) == self.l1_cap:
                evicted = self.l1_order.popleft()
                if len(self.l2) >= self.l2_cap:
                    self.l2_order.popleft()
                self.l2[evicted] = self.l1[evicted]
                self.l2_order.append(evicted)
            self.l1[key] = value
            self.l1_order.append(key)

print("=== PROBLEM 1: LRU CACHE ===")
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print("Get 1:", lru.get(1))
lru.put(3, 3)
print("Get 2 (should be -1 after evict):", lru.get(2))
print()


# ============================================================
# PROBLEM 2: MINSTACK (Bonus: MaxStack, K-th Largest Stack)
# ============================================================
# What it solves: Stack with O(1) min/max retrieval
# Strategy: Dual stack (values + mins/maxs)
# Interview angle: Get K-th largest? Range queries?

# BASE: MinStack
class MinStack:
    """Base: stack with O(1) min"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# VARIANT 2A: MaxStack (dual min)
class MaxStack:
    """Variant A: stack with O(1) max"""
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1]

# VARIANT 2B: K-th largest in stack
class KthLargestStack:
    """Variant B: get K-th largest element"""
    def __init__(self, k):
        self.stack = []
        self.k_largest = []
        self.k = k

    def push(self, val):
        self.stack.append(val)
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
        elif val > self.k_largest[0]:
            heapq.heapreplace(self.k_largest, val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def get_kth_largest(self):
        """Return k-th largest (or -1 if fewer than k elements)"""
        return self.k_largest[0] if len(self.k_largest) == self.k else -1

# VARIANT 2C: Range min/max
class RangeStack:
    """Variant C: query min/max in range [start, end]"""
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def range_min(self, start, end):
        """Min in range [start, end]"""
        if start > end or end >= len(self.stack):
            return None
        return min(self.stack[start:end+1])

    def range_max(self, start, end):
        """Max in range [start, end]"""
        if start > end or end >= len(self.stack):
            return None
        return max(self.stack[start:end+1])

print("=== PROBLEM 2: MINSTACK ===")
ms = MinStack()
for v in [3, 1, 4, 1, 5]:
    ms.push(v)
print("Top:", ms.top(), ", Min:", ms.get_min())
print()


# ============================================================
# PROBLEM 3: UNION-FIND (DISJOINT SET UNION)
# ============================================================
# What it solves: Efficient find & union of elements into components
# Use case: Connected components, cycle detection
# Optimization: Path compression + union by rank → near O(1)

# BASE: Union-Find with path compression
class UnionFind:
    """Base: union-find with path compression"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
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

    def connected(self, x, y):
        """Check if in same component"""
        return self.find(x) == self.find(y)

# VARIANT 3A: Find connected components
def find_components(uf, n):
    """Variant A: return all connected components"""
    components = defaultdict(list)
    for i in range(n):
        components[uf.find(i)].append(i)
    return list(components.values())

# VARIANT 3B: Detect cycle in graph
def has_cycle_uf(edges):
    """Variant B: detect cycle using union-find"""
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False

# VARIANT 3C: Component size tracking
class UnionFindWithSize(UnionFind):
    """Variant C: track size of each component"""
    def __init__(self, n):
        super().__init__(n)
        self.size = [1] * n

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

    def get_component_size(self, x):
        return self.size[self.find(x)]

print("=== PROBLEM 3: UNION-FIND ===")
uf = UnionFind(5)
uf.union(0, 1)
uf.union(2, 3)
print("Connected 0 and 1:", uf.connected(0, 1))
print("Connected 0 and 2:", uf.connected(0, 2))
print()


# ============================================================
# PROBLEM 4: MEDIAN FINDER
# ============================================================
# What it solves: Find median of stream of numbers
# Strategy: Two heaps (max-heap for left, min-heap for right)

# BASE: Median finder
class MedianFinder:
    """Base: find median of stream"""
    def __init__(self):
        self.small = []  # max-heap (negate values)
        self.large = []  # min-heap
        self.small_size = 0
        self.large_size = 0

    def addNum(self, num):
        if self.small_size == 0:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        elif num < -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1

        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
        elif self.large_size > self.small_size:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.small_size += 1
            self.large_size -= 1

    def findMedian(self):
        if self.small_size > self.large_size:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2

# VARIANT 4A: K-th percentile
def kth_percentile(stream, k):
    """Variant A: k-th percentile of stream"""
    sorted_stream = sorted(stream)
    idx = int(len(sorted_stream) * k / 100)
    return sorted_stream[idx]

# VARIANT 4B: Weighted median
def weighted_median(values, weights):
    """Variant B: median with weights"""
    total = sum(weights)
    sorted_pairs = sorted(zip(values, weights))
    cumsum = 0
    for val, w in sorted_pairs:
        cumsum += w
        if cumsum >= total / 2:
            return val
    return None

print("=== PROBLEM 4: MEDIAN FINDER ===")
mf = MedianFinder()
for num in [1, 2, 3, 4, 5]:
    mf.addNum(num)
print("Median:", mf.findMedian())
print()

print("=" * 70)
print("CATEGORY 9: DESIGN PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Hash + structure (LRU, LFU)")
print("Pattern 2: Dual structures (min/max stack)")
print("Pattern 3: Graph patterns (union-find)")
print("Pattern 4: Stream processing (median finder)")
print("=" * 70)
