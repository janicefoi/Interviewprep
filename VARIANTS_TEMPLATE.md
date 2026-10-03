# VARIANTS TEMPLATE FOR CATEGORIES 3-9

## CATEGORY 3: Two Pointer

**Problem: Container With Most Water**
- BASE: Find max area between two lines
- VARIANT A: Find min area (instead of max)
- VARIANT B: Count how many pairs form area >= K
- VARIANT C: Find pair closest to specific area value

**Problem: 3Sum**
- BASE: All triplets summing to 0
- VARIANT A: All triplets summing to target (not 0)
- VARIANT B: 3Sum Closest (closest to target, not exact)
- VARIANT C: Count triplets (not return them)

---

## CATEGORY 4: Stack

**Problem: Valid Parentheses**
- BASE: Check if balanced
- VARIANT A: Return depth of deepest nesting
- VARIANT B: Remove minimum chars to make valid
- VARIANT C: Score valid parentheses (1 per pair, doubles when nested)

**Problem: Next Greater Element**
- BASE: For each element, find next larger to the right
- VARIANT A: Find PREVIOUS larger (to the left)
- VARIANT B: Find closest larger (either direction)
- VARIANT C: Find k-th larger element

---

## CATEGORY 5: Binary Search

**Problem: Binary Search**
- BASE: Find exact target in sorted array
- VARIANT A: Find closest value (if exact not found)
- VARIANT B: Count occurrences of target
- VARIANT C: Find insertion position to maintain sort

**Problem: Search Rotated Sorted Array**
- BASE: Find target in rotated array
- VARIANT A: Find minimum (rotation point)
- VARIANT B: Find maximum
- VARIANT C: Count occurrences of target

---

## CATEGORY 6: Linked List

**Problem: Reverse Linked List**
- BASE: Reverse entire list
- VARIANT A: Reverse first K nodes
- VARIANT B: Reverse every K nodes (K, K, ..., remainder)
- VARIANT C: Reverse between positions M and N

**Problem: Merge Two Sorted Lists**
- BASE: Merge two lists
- VARIANT A: Merge K sorted lists (heap approach)
- VARIANT B: Merge in-place (modify one list, return it)
- VARIANT C: Merge and flatten (if lists contain lists)

---

## CATEGORY 7: Tree/Graph

**Problem: Max Depth**
- BASE: Height of tree
- VARIANT A: Max depth at each level (return array)
- VARIANT B: Count nodes at max depth
- VARIANT C: Find path to deepest node

**Problem: Level Order Traversal**
- BASE: Return nodes by level
- VARIANT A: Return levels in reverse order
- VARIANT B: Zigzag traversal (alternate directions per level)
- VARIANT C: Return only rightmost node per level

**Problem: Valid BST**
- BASE: Check if valid BST
- VARIANT A: Find first node violating BST property
- VARIANT B: Fix BST (minimal changes)
- VARIANT C: Count how many swaps needed to fix

---

## CATEGORY 8: Dynamic Programming

**Problem: Coin Change**
- BASE: Minimum coins to make amount
- VARIANT A: Count ways to make amount
- VARIANT B: Return the coins (not count)
- VARIANT C: Max coins to make amount (using all coins as many times as needed)

**Problem: Longest Common Subsequence**
- BASE: Length of LCS
- VARIANT A: Return the actual subsequence (not length)
- VARIANT B: LCS of 3 strings (not 2)
- VARIANT C: Count number of distinct LCS

**Problem: Edit Distance**
- BASE: Min edits to transform word1 to word2
- VARIANT A: Return the edits (not count)
- VARIANT B: Only insertions/deletions (no replacements)
- VARIANT C: With custom cost per operation type

---

## CATEGORY 9: Design

**Problem: LRU Cache**
- BASE: Evict least recently used
- VARIANT A: Evict least frequently used (LFU)
- VARIANT B: Time-based expiry (TTL)
- VARIANT C: Multi-tier cache (L1, L2)

**Problem: MinStack**
- BASE: Efficient min retrieval
- VARIANT A: Efficient min and max
- VARIANT B: Get k-th largest efficiently
- VARIANT C: Range min/max queries

---

## PATTERN SUMMARY

### Variant Types (across all categories)

1. **Output Change**: Boolean → Value → Count → All values
2. **Constraint Change**: No limit → K limit → Exact value
3. **Direction Change**: Forward → Backward → Both directions
4. **Aggregation Change**: Single best → All matching → Count
5. **Data Structure Change**: Hashmap → Heap → Two-pointer
6. **Generalization**: 2-sum → 3-sum → K-sum
7. **Customization**: Fixed value → Custom parameter → Variable cost

### Interview Strategy

When you see a "new" problem:
1. Identify the CORE pattern (category)
2. Check if it's a VARIANT of that pattern
3. Apply the same algorithm with the constraint twist
4. This turns a "new problem" into a "known pattern with a flag"

