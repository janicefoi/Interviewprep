# SWE Internship Interview Prep — 9 Categories with Variants

**Datadog focus:** Medium-easy Q1 (15 min) + Medium Q2 with variant twist (45 min). Master the base problems AND their variants.

---

# CATEGORY 1: Hashmap / Dict

## Core Pattern
"Check + remember" — hashmap/set for O(1) lookups and counting.

### Problem 1: Two Sum
**Base:** Find any pair summing to target
- **Variants:**
  - A: Count distinct pairs (not return them)
  - B: Return ALL pairs (not just one)
  - C: Sorted array → use two-pointer for O(1) space

### Problem 2: Three Sum
**Base:** Find all unique triplets summing to 0
- **Variants:**
  - A: Sum to custom target (not 0)
  - B: Find closest sum to target (3Sum Closest)
  - C: Count triplets (not return them)

### Problem 3: Four Sum
**Base:** Extend to 4 numbers
- **Variants:**
  - A: K-Sum (generalize to any K)
  - B: Count 4-tuples instead of returning
  - C: Custom target sum

### Problem 4: Contains Duplicate
**Base:** Any value appears twice? Return boolean
- **Variants:**
  - A: Duplicates within distance K (sliding window + set)
  - B: Return first duplicate value (not boolean)
  - C: Return all duplicate values

### Problem 5: Count All (Frequency Map)
**Base:** Build frequency dict for all values
- **Variants:**
  - A: Filter by minimum threshold (count >= K)
  - B: Top K frequent elements (use heap)
  - C: Group by frequency (invert the map)

### Problem 6: Most Frequent / Least Frequent
**Base:** Return value with highest/lowest count
- **Variants:**
  - A: Return all values at max frequency (not just one)
  - B: Return top K frequencies
  - C: Return values with exact frequency F

### Problem 7: Common Elements
**Base:** Find intersection of two lists
- **Variants:**
  - A: Find union (not intersection)
  - B: Find symmetric difference (in either, not both)
  - C: Find intersection with frequency preservation

### Problem 8: Group Anagrams
**Base:** Group strings that are anagrams
- **Variants:**
  - A: Return only groups with size >= K
  - B: Find largest anagram group
  - C: Count total anagram groups

### Problem 9: Two Sum (Sorted Array Variant)
**Base:** Sorted array → two-pointer for O(1) space
- **Variants:**
  - A: Return indices instead of values
  - B: Count how many pairs (not return them)
  - C: Find pair closest to target (not equal)

### Problem 10: Is Anagram
**Base:** Check if two strings are anagrams
- **Variants:**
  - A: Check if anagram after removing K chars
  - B: Find minimum chars to remove to make anagrams
  - C: Group anagrams by minimum edits needed

**Datadog Likelihood:** ⭐⭐⭐⭐⭐ (This is THEIR pattern)

---

# CATEGORY 2: Sliding Window

## Core Pattern
Maintain a window, expand/shrink based on constraint.

### Problem 1: Max Sum Subarray (Fixed Window)
**Base:** Max sum of K consecutive elements
- **Variants:**
  - A: Max product instead of sum
  - B: Count windows with sum >= threshold
  - C: Return all windows meeting constraint

### Problem 2: Longest Substring Without Repeating
**Base:** Length of longest substring with no duplicates
- **Variants:**
  - A: With repeats allowed (inverse constraint)
  - B: Count how many substrings have no repeats
  - C: At most K distinct characters

### Problem 3: Shortest Burst (At-Least-Threshold)
**Base:** Shortest window with sum >= threshold
- **Variants:**
  - A: Window with sum EXACTLY equal to target
  - B: Count how many windows meet constraint
  - C: Longest window (inverse of shortest)

### Problem 4: Min Window Substring
**Base:** Shortest substring containing all chars from target
- **Variants:**
  - A: Return length instead of substring
  - B: Return ALL valid windows (not just shortest)
  - C: Count how many windows contain all chars

### Problem 5: Best Time to Buy/Sell Stock
**Base:** Max profit from buy-then-sell
- **Variants:**
  - A: Multiple transactions allowed (DP + greedy)
  - B: With cooldown (can't trade consecutive days)
  - C: With transaction fee

### Problem 6: Longest Repeating Character Replacement
**Base:** Longest substring where you replace at most K chars to make all same
- **Variants:**
  - A: Return the actual substring (not length)
  - B: Minimum chars to replace (not maximum window)
  - C: Multiple different target characters

### Problem 7: Longest Substring K Distinct
**Base:** Longest with at most K distinct characters
- **Variants:**
  - A: Exactly K distinct (not at most)
  - B: Count windows with K distinct chars
  - C: Find all windows with K distinct

### Problem 8: Subarray Sum Equals K
**Base:** Count subarrays with sum exactly equal to K
- **Variants:**
  - A: Return the subarrays (not count)
  - B: Longest subarray with sum K
  - C: Shortest subarray with sum K

**Datadog Likelihood:** ⭐⭐⭐⭐⭐ (Question 2 often uses this)

---

# CATEGORY 3: Two Pointer

## Core Pattern
Pointers from both ends moving inward.

### Problem 1: Container With Most Water
**Base:** Find two lines that form container with max water
- **Variants:**
  - A: Find min area (instead of max)
  - B: Count pairs forming area >= K
  - C: Find pair closest to specific area

### Problem 2: Three Sum
**Base:** All unique triplets summing to 0
- **Variants:**
  - A: Custom target (not 0)
  - B: Closest sum to target
  - C: Count triplets (not return them)

### Problem 3: Remove Duplicates (Sorted Array)
**Base:** Remove duplicates in-place, return length
- **Variants:**
  - A: Remove at most K duplicates per value
  - B: Return the deduplicated array (not length)
  - C: Remove and collect all duplicates

### Problem 4: Valid Palindrome
**Base:** Check if string is palindrome (ignoring non-alphanumeric)
- **Variants:**
  - A: Valid palindrome after removing at most K chars
  - B: Count how many chars to remove
  - C: Find longest palindromic substring

### Problem 5: Is Sorted Rotated
**Base:** Check if array is sorted then rotated
- **Variants:**
  - A: Find rotation point (minimum position)
  - B: Count how many rotations needed
  - C: Un-rotate the array

### Problem 6: Trapping Rain Water
**Base:** Calculate trapped water between elevations
- **Variants:**
  - A: 2D grid (rain water in 2D)
  - B: Count blocks of water (not volume)
  - C: With obstacles

### Problem 7: Sort Colors (Dutch Flag)
**Base:** Partition 0s, 1s, 2s in one pass
- **Variants:**
  - A: Sort K colors (not just 3)
  - B: Minimize swaps needed
  - C: Return counts (not sort in-place)

### Problem 8: Partition Equal Subset Sum
**Base:** Can we split array into two equal-sum subsets?
- **Variants:**
  - A: Return which elements go to each subset
  - B: Minimum difference between subsets
  - C: Return indices (not values)

**Datadog Likelihood:** ⭐⭐⭐⭐ (Less common, but appears)

---

# CATEGORY 4: Stack

## Core Pattern
LIFO for matching/pairing, or monotonic stack for next-greater queries.

### Problem 1: Valid Parentheses
**Base:** Check if brackets are balanced
- **Variants:**
  - A: Return depth of deepest nesting
  - B: Remove minimum chars to make valid
  - C: Score parentheses (1 per pair, double when nested)

### Problem 2: Next Greater Element
**Base:** For each element, find next larger to the right
- **Variants:**
  - A: Find previous larger (to the left)
  - B: Find closest larger (either direction)
  - C: Find K-th larger element

### Problem 3: Daily Temperatures
**Base:** Days until warmer temperature for each day
- **Variants:**
  - A: Days until COLDER temperature
  - B: Find closest temperature (either direction)
  - C: Return temperatures (not distances)

### Problem 4: Remove Adjacent Duplicates
**Base:** Collapse adjacent matching characters
- **Variants:**
  - A: Remove duplicates appearing > K times
  - B: Return removed pairs (not collapsed string)
  - C: With custom duplicate rule (not just adjacent)

### Problem 5: Min Stack
**Base:** Stack with O(1) get_min operation
- **Variants:**
  - A: Add get_max as well
  - B: Get K-th largest
  - C: Range min/max queries

### Problem 6: Largest Rectangle in Histogram
**Base:** Find largest rectangular area
- **Variants:**
  - A: Count rectangles (not max)
  - B: Return actual rectangle dimensions
  - C: 2D histogram (max volume in 2D)

### Problem 7: Decode String
**Base:** Decode pattern like 3[a2[c]] → acaca
- **Variants:**
  - A: Encode a string (reverse operation)
  - B: Count total decoded length (not decode)
  - C: With custom encoding rules

### Problem 8: Simplify Path
**Base:** Simplify Unix path (resolve . and ..)
- **Variants:**
  - A: Return canonical path
  - B: Count directory levels
  - C: Find common ancestor path

**Datadog Likelihood:** ⭐⭐⭐ (Moderate; mostly in senior rounds)

---

# CATEGORY 5: Binary Search

## Core Pattern
O(log n) on sorted/nearly-sorted data.

### Problem 1: Binary Search
**Base:** Find exact target in sorted array
- **Variants:**
  - A: Find closest value (if exact not found)
  - B: Count occurrences of target
  - C: Find insertion position

### Problem 2: Search Rotated Sorted Array
**Base:** Find target in rotated array
- **Variants:**
  - A: Find minimum (rotation point)
  - B: Find maximum
  - C: Count occurrences

### Problem 3: Find Peak
**Base:** Find peak element (> both neighbors)
- **Variants:**
  - A: Find all peaks
  - B: Find valley (< both neighbors)
  - C: Count peaks

### Problem 4: Sqrt(x)
**Base:** Integer square root
- **Variants:**
  - A: Cube root
  - B: K-th root
  - C: Find closest perfect square

### Problem 5: First/Last Position
**Base:** Find leftmost occurrence of target
- **Variants:**
  - A: Find rightmost occurrence
  - B: Count total occurrences
  - C: Find both leftmost and rightmost

### Problem 6: Min in Rotated Array
**Base:** Find minimum in rotated sorted array
- **Variants:**
  - A: Find maximum
  - B: Find rotation count
  - C: Handle duplicates

### Problem 7: Capacity to Ship (Binary Search on Answer)
**Base:** Minimum capacity to ship in D days
- **Variants:**
  - A: Maximum weight per package constraint
  - B: Custom shipping cost calculation
  - C: Multiple vehicles

### Problem 8: Find K Closest Elements
**Base:** K closest to target in sorted array
- **Variants:**
  - A: K farthest (instead of closest)
  - B: Return sorted (not array order)
  - C: Custom distance metric

**Datadog Likelihood:** ⭐⭐⭐⭐ (Common but less so than Categories 1-2)

---

# CATEGORY 6: Linked List

## Core Pattern
Pointer manipulation, two-pointer (slow/fast).

### Problem 1: Reverse Linked List
**Base:** Reverse entire list
- **Variants:**
  - A: Reverse first K nodes
  - B: Reverse every K nodes (groups)
  - C: Reverse between positions M and N

### Problem 2: Merge Two Sorted Lists
**Base:** Merge two sorted lists
- **Variants:**
  - A: Merge K sorted lists (use heap)
  - B: Merge in-place
  - C: Merge and remove duplicates

### Problem 3: Has Cycle
**Base:** Detect if list has cycle
- **Variants:**
  - A: Find cycle start node
  - B: Return cycle length
  - C: Find node at cycle intersection

### Problem 4: Find Middle
**Base:** Return middle node (slow/fast pointers)
- **Variants:**
  - A: Return all middle nodes (if even length)
  - B: Find K-th from end
  - C: Find nth percentile node

### Problem 5: Remove Nth From End
**Base:** Remove nth node from end
- **Variants:**
  - A: Remove all occurrences of value
  - B: Remove and return the node
  - C: Remove pairs of nodes

### Problem 6: Is Palindrome (Linked List)
**Base:** Check if list values form palindrome
- **Variants:**
  - A: Return palindromic part (not boolean)
  - B: Count minimum edits to make palindrome
  - C: Find longest palindromic sublist

### Problem 7: Reorder List
**Base:** Reorder [1,2,3,4] → [1,4,2,3]
- **Variants:**
  - A: Reorder alternating (1, n, 2, n-1, ...)
  - B: Return interleaved lists (not modify)
  - C: Custom reordering pattern

### Problem 8: Intersection of Two Lists
**Base:** Find node where two lists intersect
- **Variants:**
  - A: Return intersection value (not node)
  - B: Return distance to intersection
  - C: Handle multiple intersections

**Datadog Likelihood:** ⭐⭐⭐ (Less common, but appears)

---

# CATEGORY 7: Tree / Graph

## Core Pattern
BFS/DFS, recursion, tree traversal.

### Problem 1: Max Depth
**Base:** Height of binary tree
- **Variants:**
  - A: Max depth at each level
  - B: Count nodes at max depth
  - C: Path to deepest node

### Problem 2: Level Order Traversal
**Base:** Return nodes grouped by level
- **Variants:**
  - A: Return levels in reverse
  - B: Zigzag traversal
  - C: Return rightmost node per level

### Problem 3: Validate BST
**Base:** Check if valid binary search tree
- **Variants:**
  - A: Find first violating node
  - B: Minimum changes to fix
  - C: Count swaps needed

### Problem 4: Number of Islands
**Base:** Count islands in 2D grid
- **Variants:**
  - A: Find largest island size
  - B: Return all island coordinates
  - C: Count with diagonal connectivity

### Problem 5: Has Path (Graph)
**Base:** Check if path exists from start to end
- **Variants:**
  - A: Return the path (not boolean)
  - B: Shortest path (BFS)
  - C: All paths from start to end

### Problem 6: Lowest Common Ancestor
**Base:** Find LCA of two nodes
- **Variants:**
  - A: LCA with K nodes (not 2)
  - B: Distance between two nodes
  - C: All ancestors of node

### Problem 7: Path Sum
**Base:** Root-to-leaf paths summing to target
- **Variants:**
  - A: Count paths (not return them)
  - B: Return individual path sums
  - C: Max path sum (any node to any node)

### Problem 8: Inorder/Preorder/Postorder
**Base:** Tree traversal in specific order
- **Variants:**
  - A: Return in opposite order (reverse)
  - B: Count nodes at each traversal step
  - C: Build tree from traversals

**Datadog Likelihood:** ⭐⭐⭐⭐ (Common in senior rounds)

---

# CATEGORY 8: Dynamic Programming

## Core Pattern
Break problem into overlapping subproblems, memoize/table-build.

### Problem 1: Climb Stairs
**Base:** Ways to climb n stairs (1 or 2 at a time)
- **Variants:**
  - A: With custom step sizes
  - B: Return actual paths (not count)
  - C: With obstacle positions

### Problem 2: Coin Change
**Base:** Minimum coins to make amount
- **Variants:**
  - A: Count ways (not minimum)
  - B: Return the coins (not count)
  - C: Maximum coins allowed

### Problem 3: LCS (Longest Common Subsequence)
**Base:** Length of longest common subsequence
- **Variants:**
  - A: Return actual subsequence
  - B: LCS of 3+ strings (not 2)
  - C: Count distinct LCS

### Problem 4: Edit Distance
**Base:** Min edits to transform word1 to word2
- **Variants:**
  - A: Return the edits (not count)
  - B: Only insertions/deletions (no replacements)
  - C: Custom cost per operation

### Problem 5: Longest Increasing Subsequence
**Base:** Length of longest strictly increasing subsequence
- **Variants:**
  - A: Return actual subsequence
  - B: Count distinct LIS
  - C: Longest non-decreasing (not strict)

### Problem 6: Max Subarray (Kadane)
**Base:** Max sum of contiguous subarray
- **Variants:**
  - A: Return the subarray (not sum)
  - B: Max product subarray
  - C: Closest to K (not maximum)

### Problem 7: Knapsack 0/1
**Base:** Max value with weight constraint (each item once)
- **Variants:**
  - A: Return which items (not value)
  - B: Unbounded knapsack (items reusable)
  - C: Fractional knapsack

### Problem 8: House Robber
**Base:** Max money robbing houses (can't rob adjacent)
- **Variants:**
  - A: Return which houses (not total)
  - B: Houses in circle (first/last connected)
  - C: With custom constraint (can rob at most K)

### Problem 9: Partition Equal Subset Sum
**Base:** Can split into two equal-sum subsets?
- **Variants:**
  - A: Return which elements per subset
  - B: Minimum difference between subsets
  - C: Partition into K subsets

**Datadog Likelihood:** ⭐⭐⭐ (Often Q2 follow-up, less so main)

---

# CATEGORY 9: Design

## Core Pattern
Combine multiple data structures for O(1) operations.

### Problem 1: LRU Cache
**Base:** Evict least recently used, O(1) get/put
- **Variants:**
  - A: Evict least frequently used (LFU)
  - B: Time-based expiry (TTL)
  - C: Multi-tier cache (L1, L2)

### Problem 2: MinStack
**Base:** Stack with O(1) min retrieval
- **Variants:**
  - A: Add max retrieval too
  - B: Get K-th largest efficiently
  - C: Range min/max

### Problem 3: Union-Find
**Base:** Efficient find/union with path compression
- **Variants:**
  - A: Weighted union-find
  - B: Find connected components
  - C: Detect cycle in graph

### Problem 4: Median Finder
**Base:** Stream median using dual heaps
- **Variants:**
  - A: Running median
  - B: Median after removing elements
  - C: K-th percentile (not median)

### Problem 5: Randomized Set
**Base:** Insert/remove/random in O(1)
- **Variants:**
  - A: With weights (random weighted selection)
  - B: Skip element on removal
  - C: K random elements

### Problem 6: Time-Based Key-Value Store
**Base:** Get value for key at specific timestamp
- **Variants:**
  - A: Return all changes between times
  - B: Closest timestamp (before/after)
  - C: Custom query time windows

### Problem 7: LFU Cache
**Base:** Evict least frequently used (harder than LRU)
- **Variants:**
  - A: Return eviction order
  - B: Access patterns analytics
  - C: Custom frequency calculation

**Datadog Likelihood:** ⭐⭐⭐⭐ (LRU especially; appears in system design rounds)

---

# Interview Strategy

## How Variants Show Up

1. **Q1 (15 min):** BASE problem
   - "Implement Two Sum"
   - "Reverse a Linked List"
   - "Longest Substring Without Repeating"

2. **Q2 Follow-up (45 min):** VARIANT with twist
   - "What if we need to return ALL pairs, not just one?"
   - "What if we add a distance constraint?"
   - "What if we need to use only O(1) space?"
   - "What if the input is sorted?"

## Three-Step Interview Approach

**Step 1: Identify Core Pattern**
- Is it Hashmap? Two Pointer? DP?
- Which category does it match?

**Step 2: Recognize the Variant**
- Output change? (boolean → value → count → all)
- Constraint added? (distance, frequency, threshold)
- Data structure required? (sorted → two-pointer)

**Step 3: Adapt Algorithm**
- Core logic stays same
- Only output, constraint, or data structure changes
- You've already solved this exact variant before

## Confidence Boosters

- ✅ You know all 9 base patterns
- ✅ You know 3-4 variants per pattern
- ✅ You can recognize variants on sight
- ✅ You can adapt in real time during interview

---

# File Structure in Your Folder

```
✅ Category1_HashmapDict_WITH_VARIANTS.py (code + variants)
✅ Category2_SlidingWindow_WITH_VARIANTS.py (code + variants)
✅ Category3_TwoPointer.py through Category9_Design.py (base code)
📖 INTERVIEW_PREP_GUIDE.md (THIS FILE — all categories + variants)
```

---

# Next Steps

1. **Study this guide** — understand all 9 categories
2. **Run the variant files** — see how variants work in code
3. **Code your own variants** — for Categories 3-9 using the blueprint above
4. **Practice variants** — when interviewer asks "what if", you're ready

---

# Good luck with Datadog! 🚀

Every "new" problem is just a variant of something you already know.
