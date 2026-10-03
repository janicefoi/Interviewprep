# Datadog SWE Internship Interview — Complete 9-Category Guide

**Target:** Medium-easy Q1 (15 min) + Medium Q2 with variant twist (45 min)  
**Strategy:** Master base problems + recognize variants + adapt in real time

---

# CATEGORY 1: HASHMAP / DICT

## Core Pattern: "Check + Remember"
Use hashmap/set for O(1) lookups. Build frequency maps. Answer questions by scanning the map.

### Problem 1: Two Sum
**What it solves:** Find any pair of numbers that sum to target.

**BASE:**
```
Input: [2, 7, 11, 15], target = 9
Output: [2, 7]
Time: O(n), Space: O(n)
```
Algorithm: Loop through numbers, for each check if (target - number) exists in seen set.

**VARIANTS:**
- **1A: Count distinct pairs** — How many different pairs sum to target? (Not return them)
- **1B: Return ALL pairs** — Return every unique pair, deduplicated
- **1C: Sorted array** — Use two-pointer instead of hashmap (O(1) space)

### Problem 2: Three Sum
**What it solves:** Find ALL unique triplets summing to target (usually 0).

**BASE:**
```
Input: [-1, 0, 1, 2, -1, -4], target = 0
Output: [[-1, -1, 2], [-1, 0, 1]]
Time: O(n²), Space: O(1) excluding output
```
Algorithm: Sort → for each number, reduce to two-sum problem → deduplicate at every level.

**VARIANTS:**
- **2A: Four Sum** — Generalize to 4 numbers with custom target
- **2B: Closest sum** — Find triplet whose sum is CLOSEST to target (not exact)
- **2C: Count only** — Return count of triplets, not the triplets themselves

### Problem 3: Contains Duplicate
**What it solves:** Check if any value appears more than once.

**BASE:**
```
Input: [1, 2, 3, 2]
Output: True (2 appears twice)
Time: O(n), Space: O(n)
```
Algorithm: Scan through, check if seen in set. Return true on first duplicate.

**VARIANTS:**
- **3A: Within distance K** — Are there two identical numbers within distance K of each other?
- **3B: First duplicate value** — Return the first duplicate value found (not just boolean)
- **3C: All duplicates** — Return list of all values that appear more than once

### Problem 4: Count All (Frequency Map)
**What it solves:** Build frequency dictionary showing how many times each value appears.

**BASE:**
```
Input: [1, 2, 2, 3, 2, 1]
Output: {1: 2, 2: 3, 3: 1}
Time: O(n), Space: O(k) where k = distinct values
```
Algorithm: Loop through, increment count for each number.

**VARIANTS:**
- **4A: Filter by threshold** — Return only values appearing ≥ K times
- **4B: Top K frequent** — Return K most frequent values (use heap)
- **4C: Group by frequency** — Invert map: frequency → list of values

### Problem 5: Group Anagrams
**What it solves:** Group strings that are anagrams together.

**BASE:**
```
Input: ['eat', 'tea', 'ate', 'tan', 'nat', 'bat']
Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
Time: O(n*k log k) where k = avg word length
```
Algorithm: Use sorted form of each string as key. Two anagrams have same sorted form.

**VARIANTS:**
- **5A: Size filter** — Return only groups with ≥ K strings
- **5B: Largest group** — Find the anagram group with most members
- **5C: Count groups** — Return total number of anagram groups

### Problem 6: Most Frequent / Least Frequent
**What it solves:** Find value that appears most often (or least often).

**BASE:**
```
Input: [1, 1, 1, 2, 2, 3]
Output: 1 (appears 3 times)
Time: O(n), Space: O(n)
```
Algorithm: Build frequency map → scan for max/min count.

**VARIANTS:**
- **6A: All at max frequency** — Return all values tied at highest frequency
- **6B: Top K frequencies** — Return top K frequency values themselves
- **6C: Exact frequency F** — Return values appearing exactly F times

### Problem 7: Common Elements (Intersection)
**What it solves:** Find elements appearing in both lists.

**BASE:**
```
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]
Time: O(n + m), Space: O(min(n, m))
```
Algorithm: Build set from first list → loop second list, collect items in set.

**VARIANTS:**
- **7A: Union** — Elements in either list (not both)
- **7B: Symmetric difference** — Elements in one list but not both
- **7C: Preserve frequency** — If element appears twice in list1 and 3x in list2, include twice

### Problem 8: Is Anagram
**What it solves:** Check if two strings are anagrams (same letters, same counts).

**BASE:**
```
Input: 'listen', 'silent'
Output: True
Time: O(n), Space: O(n)
```
Algorithm: Build frequency map for s1 → verify s2 "consumes" exactly those frequencies.

**VARIANTS:**
- **8A: After K removals** — Can you make anagrams by removing ≤ K chars from each?
- **8B: Min removals** — Minimum total chars to remove to make anagrams
- **8C: Edit distance** — Minimum insert/delete operations to transform s1 to s2

**Interview Tip for Category 1:**  
Hashmap problems are about **pattern recognition**. Most variants just change:
- Output format (boolean → value → count → all)
- Constraint (distance K, frequency threshold, custom target)
- Data structure (dict → heap → sorted array)

---

# CATEGORY 2: SLIDING WINDOW

## Core Pattern: Maintain window, expand/shrink based on constraint
Fixed-size windows slide across. Variable-size windows grow/shrink to satisfy condition.

### Problem 1: Max Sum Subarray (Fixed Window)
**What it solves:** Find maximum sum of K consecutive elements.

**BASE:**
```
Input: [2, 1, 5, 1, 3, 2], K=3
Output: 9 (window [5, 1, 3])
Time: O(n), Space: O(1)
```
Algorithm: Compute sum of first K elements. Then slide: add new element, remove old element.

**VARIANTS:**
- **1A: Product instead of sum** — Maximum product of K consecutive numbers
- **1B: Count windows** — How many K-windows have sum ≥ threshold?
- **1C: Return all** — Return all windows with sum ≥ threshold (not just max)

### Problem 2: Longest Substring Without Repeating
**What it solves:** Length of longest substring with no duplicate characters.

**BASE:**
```
Input: 'abcabcbb'
Output: 3 (substring 'abc')
Time: O(n), Space: O(k) where k = alphabet size
```
Algorithm: Two pointers + char → index map. When duplicate found, move left pointer.

**VARIANTS:**
- **2A: With repeats (inverse)** — Longest substring with AT LEAST one repeat
- **2B: Count substrings** — How many substrings have no repeats?
- **2C: At most K distinct** — Longest substring with ≤ K distinct characters

### Problem 3: Shortest Window with Sum ≥ Threshold
**What it solves:** Find shortest contiguous subarray with sum ≥ threshold.

**BASE:**
```
Input: [2, 3, 1, 2, 4, 3], threshold=7
Output: 2 (window [4, 3])
Time: O(n), Space: O(1)
```
Algorithm: Two pointers. When sum ≥ threshold, record length and shrink left. Otherwise expand right.

**VARIANTS:**
- **3A: Exact sum** — Shortest window with sum EXACTLY equal to target
- **3B: Count windows** — How many windows have sum ≥ threshold?
- **3C: Longest window** — Inverse: longest window with sum ≥ threshold

### Problem 4: Min Window Substring
**What it solves:** Shortest substring containing all characters from target string.

**BASE:**
```
Input: 'ADOBECODEBANC', target='ABC'
Output: 'BANC'
Time: O(n + m), Space: O(k) where k = alphabet size
```
Algorithm: Two pointers + frequency maps. Expand right until all chars in window. Shrink left while valid.

**VARIANTS:**
- **4A: Return length** — Only return length, not substring
- **4B: All windows** — Return ALL valid windows (not just shortest)
- **4C: Count windows** — How many windows contain all chars?

### Problem 5: Best Time to Buy and Sell Stock
**What it solves:** Maximum profit from one buy-sell transaction.

**BASE:**
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5 (buy at 1, sell at 6)
Time: O(n), Space: O(1)
```
Algorithm: Track minimum price seen so far. For each price, profit = price - min_so_far.

**VARIANTS:**
- **5A: Multiple transactions** — Can buy/sell multiple times (unlimited)
- **5B: With cooldown** — Can't trade on consecutive days
- **5C: With fee** — Each transaction costs a fee

### Problem 6: Longest Repeating Character Replacement
**What it solves:** Longest substring where you replace ≤ K chars to make all same character.

**BASE:**
```
Input: 'ABAB', K=2
Output: 4 (replace two A's with B's → 'BBBB')
Time: O(n), Space: O(k) where k = alphabet size
```
Algorithm: Expand window, track max frequency of any char in window. If (window_length - max_freq) > K, shrink.

**VARIANTS:**
- **6A: Return substring** — Return actual substring (not just length)
- **6B: Inverse** — Minimum chars to replace (not maximum window)
- **6C: Multiple targets** — Can make window all one of several characters

**Interview Tip for Category 2:**  
Sliding window problems are about **finding boundaries**. Key variants:
- Fixed vs variable window
- Exact condition vs threshold condition (== vs >=)
- Output format (length → substring → count → all)

---

# CATEGORY 3: TWO POINTER

## Core Pattern: Pointers from opposite ends moving inward
Use when: sorted arrays, need to avoid nested loops, or track two separate indices.

### Problem 1: Container With Most Water
**What it solves:** Two vertical lines form container. Find max water area.

**BASE:**
```
Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49 (lines at height 8 and 7, distance 7, water = min(8,7)*7 = 49)
Time: O(n), Space: O(1)
```
Algorithm: Two pointers at ends. Water = min(height[left], height[right]) × distance. Move SHORTER pointer (only way to improve).

**VARIANTS:**
- **1A: Min area** — Find minimum area container
- **1B: Count pairs** — How many pairs form area ≥ K?
- **1C: Closest to target** — Find pair with area closest to target area

### Problem 2: Three Sum
**What it solves:** Find all unique triplets summing to target.

**BASE:**
```
Input: [-1, 0, 1, 2, -1, -4], target=0
Output: [[-1, -1, 2], [-1, 0, 1]]
Time: O(n²), Space: O(1) excluding output
```
Algorithm: Sort → for each number i, use two-pointer to find pairs summing to -i → deduplicate.

**VARIANTS:**
- **2A: Custom target** — Sum to target T (not 0)
- **2B: Closest sum** — Triplet with sum closest to target
- **2C: Count only** — Return count of triplets, not triplets themselves

### Problem 3: Remove Duplicates (Sorted Array)
**What it solves:** Remove duplicates IN-PLACE from sorted array.

**BASE:**
```
Input: [1, 1, 1, 2, 2, 3]
Output: [1, 2, 3] (length 3)
Time: O(n), Space: O(1)
```
Algorithm: Write pointer (where to place next unique) and read pointer. When read ≠ write, advance write.

**VARIANTS:**
- **3A: Allow K duplicates** — Keep at most K of each value
- **3B: Return array** — Return deduplicated array (not just length)
- **3C: Collect duplicates** — Return all values that appeared > once

### Problem 4: Valid Palindrome
**What it solves:** Check if string is palindrome (ignore non-alphanumeric).

**BASE:**
```
Input: 'A man, a plan, a canal: Panama'
Output: True
Time: O(n), Space: O(n) for cleaned string
```
Algorithm: Clean (lowercase, alphanumeric only) → two pointers from ends, compare characters.

**VARIANTS:**
- **4A: After K removals** — Palindrome after removing ≤ K characters?
- **4B: Min removals** — Minimum characters to remove to make palindrome
- **4C: Substring check** — Is substring s[start:end] a palindrome?

### Problem 5: Partition Array (Dutch Flag)
**What it solves:** Partition array into three groups: 0s, 1s, 2s (in-place).

**BASE:**
```
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Time: O(n), Space: O(1)
```
Algorithm: Three pointers (left for 0s, mid for 1s, right for 2s). Swap carefully.

**VARIANTS:**
- **5A: K colors** — Partition into K colors (not just 3)
- **5B: Min swaps** — Minimum swaps needed to partition
- **5C: Return counts** — Return count of each color (not sort in-place)

### Problem 6: Trapping Rain Water
**What it solves:** Calculate volume of water trapped between elevations.

**BASE:**
```
Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Time: O(n), Space: O(1)
```
Algorithm: Two pointers from ends, track left_max and right_max. Water at position = min(left_max, right_max) - height.

**VARIANTS:**
- **6A: 2D grid** — Trapped water in 2D elevation grid
- **6B: Count units** — Count individual water units (same as volume)

**Interview Tip for Category 3:**  
Two-pointer is about **elimination**. Variants often change:
- Direction (left/right, forward/backward)
- What you're optimizing (max → min, count, verify)
- Output (boolean → value → count → all)

---

# CATEGORY 4: STACK

## Core Pattern: LIFO for pattern matching OR monotonic stack for efficiency
Use when: nested structures, next-greater queries, or need to "rewind" decisions.

### Problem 1: Valid Parentheses
**What it solves:** Check if brackets are balanced and properly nested.

**BASE:**
```
Input: '({[]})'
Output: True
Time: O(n), Space: O(n)
```
Algorithm: Push opening brackets. Pop and match on closing brackets. Stack empty at end = valid.

**VARIANTS:**
- **1A: Score** — Score = 1 per pair, 2x when nested. '(())' = 4
- **1B: Min removals** — Minimum characters to remove to make valid
- **1C: Min insertions** — Minimum characters to insert to make valid
- **1D: Min swaps** — Minimum adjacent swaps to balance (only () allowed)
- **1E: Longest valid** — Length of longest valid parentheses substring
- **1F: Unmatched indices** — Find indices of unmatched brackets

### Problem 2: Remove Adjacent Duplicates
**What it solves:** Collapse adjacent matching characters recursively.

**BASE:**
```
Input: 'abbaca'
Output: 'ca' (aa's cancel, then bb's cancel, then aa's cancel)
Time: O(n), Space: O(n)
```
Algorithm: Stack. If top == current, pop (they cancel). Else push.

**VARIANTS:**
- **2A: K duplicates** — Collapse when char appears ≥ K consecutive times
- **2B: Collect pairs** — Return list of (char, char) pairs that were removed
- **2C: Custom rule** — Remove based on custom function (not just equality)

### Problem 3: MinStack
**What it solves:** Stack supporting push, pop, top, AND get_min in O(1).

**BASE:**
```
push(3), push(1), push(4), push(1), push(5)
top() = 5, get_min() = 1
Time: O(1) per operation, Space: O(n)
```
Algorithm: Dual stack. Main stack holds values. Min stack holds current minimums.

**VARIANTS:**
- **3A: MaxStack** — Also track maximum value
- **3B: K-th largest** — Get K-th largest element in stack
- **3C: Range queries** — Query min/max over indices [start, end]

### Problem 4: Next Greater Element
**What it solves:** For each element, find next larger element to the right.

**BASE:**
```
Input: [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Time: O(n), Space: O(n)
```
Algorithm: Monotonic stack (decreasing). Process RIGHT to LEFT. When current > stack top, that's next-greater.

**VARIANTS:**
- **4A: Previous greater** — Next greater to the LEFT
- **4B: Circular array** — Next greater wrapping around
- **4C: Distance** — Return index difference to next-greater (not value)

### Problem 5: Daily Temperatures
**What it solves:** Days until warmer temperature for each day.

**BASE:**
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Time: O(n), Space: O(n)
```
Algorithm: Monotonic stack of indices (decreasing temps). Record distance when current > stack top.

**VARIANTS:**
- **5A: Days until cooler** — Cooler temperature (inverse)
- **5B: Actual temp** — Return next warmer temp value (not days)
- **5C: Threshold** — Days until temp ≥ threshold

**Interview Tip for Category 4:**  
Stack problems pivot on two patterns:
1. **Pattern matching** (parentheses, duplicates) — use stack to track pairs
2. **Monotonic queries** (next-greater, daily temps) — use monotonic stack

---

# CATEGORY 5: BINARY SEARCH

## Core Pattern: O(log n) by eliminating half the search space each iteration
Use when: sorted arrays OR searching on answer space (feasibility condition).

### Problem 1: Binary Search
**What it solves:** Find exact target in sorted array.

**BASE:**
```
Input: [1, 3, 5, 7, 9], target=7
Output: 3
Time: O(log n), Space: O(1)
```
Algorithm: Classic binary search. Compare mid with target, adjust bounds.

**VARIANTS:**
- **1A: Closest** — Find value closest to target (if exact not found)
- **1B: Count occurrences** — How many times target appears (with duplicates)
- **1C: Insert position** — Where to insert target to keep sorted?
- **1D: First occurrence** — Leftmost index of target (with duplicates)

### Problem 2: Search in Rotated Sorted Array
**What it solves:** Find target in array that was sorted then rotated.

**BASE:**
```
Input: [4, 5, 6, 7, 0, 1, 2], target=0
Output: 4
Time: O(log n), Space: O(1)
```
Algorithm: One half is always sorted. Check if target in sorted half. Search there or other half.

**VARIANTS:**
- **2A: Find minimum** — Find min element (rotation point)
- **2B: Find maximum** — Find max element
- **2C: With duplicates** — Count target (duplicates allowed)

### Problem 3: Find Peak Element
**What it solves:** Find index of peak (element > both neighbors).

**BASE:**
```
Input: [1, 2, 3, 1]
Output: 2 (element 3 is peak)
Time: O(log n), Space: O(1)
```
Algorithm: Compare mid with right neighbor. Move toward larger side.

**VARIANTS:**
- **3A: All peaks** — Find all peak indices
- **3B: Valley** — Find valley (inverse of peak)
- **3C: Count** — Count total peaks

### Problem 4: Sqrt(x)
**What it solves:** Integer square root (largest int where int² ≤ x).

**BASE:**
```
Input: 8
Output: 2 (since 2² = 4 ≤ 8 < 3² = 9)
Time: O(log x), Space: O(1)
```
Algorithm: Binary search on answer space. Check if mid² ≤ x.

**VARIANTS:**
- **4A: Cube root** — Integer cube root
- **4B: K-th root** — K-th root of x
- **4C: Closest square** — Closest perfect square to x

### Problem 5: Capacity to Ship (Binary Search on Answer Space)
**What it solves:** Minimum ship capacity to deliver all packages in D days.

**BASE:**
```
Input: weights=[1,2,3,4,5,6,7,8,9,10], days=5
Output: 15 (capacity needed to ship in 5 days)
Time: O(n log(sum)), Space: O(1)
```
Algorithm: Search on ANSWER SPACE (capacity), not input. For each capacity, check if feasible (greedy).

**VARIANTS:**
- **5A: Max weight constraint** — Each package ≤ max weight
- **5B: Multiple ships** — Optimal distribution with multiple ships

**Interview Tip for Category 5:**  
Binary search works on:
1. **Input space** (sorted array) — find value/position
2. **Answer space** (capacity, threshold) — find boundary where feasible ← harder!

---

# CATEGORY 6: LINKED LIST

## Core Pattern: Pointer manipulation (can't index backward, limited info)
Use when: need to modify structure in-place, or detect cycles with O(1) space.

### Problem 1: Reverse Linked List
**What it solves:** Reverse entire list in-place.

**BASE:**
```
Input: 1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1
Time: O(n), Space: O(1)
```
Algorithm: Three pointers (prev, curr, next). Reverse one link at a time.

**VARIANTS:**
- **1A: First K nodes** — Reverse only first K nodes
- **1B: Every K nodes** — Reverse each group of K nodes
- **1C: Between M and N** — Reverse only between positions M and N

### Problem 2: Merge Two Sorted Lists
**What it solves:** Merge two sorted lists into one sorted list.

**BASE:**
```
Input: 1→2→4, 1→3→4
Output: 1→1→2→3→4→4
Time: O(n + m), Space: O(1)
```
Algorithm: Two pointers, compare heads, attach smaller, advance.

**VARIANTS:**
- **2A: K sorted lists** — Merge K lists (use heap or divide-and-conquer)
- **2B: Remove duplicates** — Merge and remove duplicate values
- **2C: In-place** — Modify input lists (same as base)

### Problem 3: Has Cycle
**What it solves:** Detect if linked list has cycle.

**BASE:**
```
Input: 1→2→3→2 (cycle)
Output: True
Time: O(n), Space: O(1)
```
Algorithm: Slow/fast pointers. If they meet, cycle exists.

**VARIANTS:**
- **3A: Find cycle start** — Return node where cycle begins
- **3B: Cycle length** — Return length of cycle
- **3C: Intersection node** — Return node where slow and fast meet

### Problem 4: Find Middle Node
**What it solves:** Return middle node (or second middle if even length).

**BASE:**
```
Input: 1→2→3→4→5
Output: 3 (middle node)
Time: O(n), Space: O(1)
```
Algorithm: Slow/fast pointers. Fast goes 2x speed.

**VARIANTS:**
- **4A: K-th from end** — Find node K positions from end
- **4B: All middles** — Return both middle nodes if even length
- **4C: Percentile** — Find node at nth percentile

### Problem 5: Remove Nth From End
**What it solves:** Remove n-th node from end of list.

**BASE:**
```
Input: 1→2→3→4→5, n=2
Output: 1→2→3→5 (removed node 4)
Time: O(n), Space: O(1)
```
Algorithm: Two-pass with dummy node. First find length, then remove.

**VARIANTS:**
- **5A: All occurrences** — Remove ALL nodes with specific value
- **5B: Return node** — Remove node AND return it
- **5C: Remove pairs** — Remove nodes in pairs

**Interview Tip for Category 6:**  
Linked list problems require:
- Careful pointer management (prev, curr, next tracking)
- Dummy node for edge cases (removing head)
- Slow/fast two-pointer for O(1) space

---

# CATEGORY 7: TREE / GRAPH

## Core Pattern: BFS/DFS traversal with careful state tracking
Use when: need to visit nodes in order, find connectivity, or traverse structure.

### Problem 1: Max Depth (Height)
**What it solves:** Find maximum depth (height) of binary tree.

**BASE:**
```
Input: Tree with root 3, left=9, right=20
Output: 3
Time: O(n), Space: O(h) where h=height
```
Algorithm: Recursion. max_depth = 1 + max(left_depth, right_depth).

**VARIANTS:**
- **1A: Min depth** — Shortest path to leaf
- **1B: Count at max** — How many nodes at maximum depth?
- **1C: Path to deepest** — Return path (list of values) to deepest node

### Problem 2: Level Order Traversal
**What it solves:** Return nodes grouped by level (BFS).

**BASE:**
```
Input: [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
Time: O(n), Space: O(w) where w=max width
```
Algorithm: Queue. Process level by level.

**VARIANTS:**
- **2A: Reverse levels** — Levels in reverse order
- **2B: Zigzag** — Left-to-right, right-to-left, alternating
- **2C: Rightmost** — Return rightmost node per level

### Problem 3: Validate BST
**What it solves:** Check if binary tree is valid BST.

**BASE:**
```
Input: Tree with 2, left=1, right=3
Output: True (valid BST)
Time: O(n), Space: O(h)
```
Algorithm: Track valid range for each node. For left child: upper bound = parent. For right: lower bound = parent.

**VARIANTS:**
- **3A: Find violating node** — First node that violates BST property
- **3B: Min changes** — Minimum node value changes to make valid
- **3C: Count swaps** — Swaps needed to fix (inorder vs sorted)

### Problem 4: Number of Islands
**What it solves:** Count disconnected regions of 1s in 2D grid.

**BASE:**
```
Input: [['1','1','0'], ['0','1','0'], ['1','0','1']]
Output: 3
Time: O(m*n), Space: O(m*n) for visited
```
Algorithm: DFS/BFS. Mark visited cells, count regions.

**VARIANTS:**
- **4A: Largest island** — Area of largest island
- **4B: All coordinates** — Return coordinates of all islands
- **4C: Diagonal connectivity** — Count with 8-directional connectivity

**Interview Tip for Category 7:**  
Tree/graph problems need:
- Careful recursion or queue management
- Proper base cases (null checks, leaf detection)
- State tracking (visited sets, valid ranges)

---

# CATEGORY 8: DYNAMIC PROGRAMMING

## Core Pattern: Break into overlapping subproblems, memoize results
Use when: optimal substructure exists and decision recurs.

### Problem 1: Climb Stairs
**What it solves:** Ways to climb n stairs taking 1 or 2 steps at a time.

**BASE:**
```
Input: n=5
Output: 8
f(n) = f(n-1) + f(n-2) (Fibonacci!)
Time: O(n), Space: O(1)
```
Algorithm: DP[i] = DP[i-1] + DP[i-2]. Base: DP[1]=1, DP[2]=2.

**VARIANTS:**
- **1A: Custom steps** — With step sizes [1, 2, 3, ...] 
- **1B: Return paths** — Return all possible paths (combinations)
- **1C: With obstacles** — Skip specific step positions

### Problem 2: Coin Change
**What it solves:** Minimum coins to make amount (unbounded — reuse coins).

**BASE:**
```
Input: coins=[1,2,5], amount=5
Output: 1 (one 5-coin)
Time: O(amount * len(coins)), Space: O(amount)
```
Algorithm: DP[i] = min(DP[i-coin] + 1) for all coins.

**VARIANTS:**
- **2A: Count ways** — How many ways to make amount?
- **2B: Return coins** — Which coins to use?
- **2C: Limited coins** — Each coin used at most once (0/1 knapsack)

### Problem 3: Longest Common Subsequence
**What it solves:** Length of longest subsequence common to both strings.

**BASE:**
```
Input: 'abcde', 'ace'
Output: 3 ('ace' is LCS)
Time: O(m*n), Space: O(m*n)
```
Algorithm: 2D DP. DP[i][j] = LCS of s1[0:i] and s2[0:j].

**VARIANTS:**
- **3A: Return string** — Return actual LCS string (not just length)
- **3B: K strings** — LCS of multiple strings
- **3C: Count distinct** — How many distinct LCS exist?

### Problem 4: Edit Distance
**What it solves:** Minimum edits (insert/delete/replace) to transform s1 to s2.

**BASE:**
```
Input: 'horse', 'ros'
Output: 3 (h→delete, e→delete)
Time: O(m*n), Space: O(m*n)
```
Algorithm: 2D DP. DP[i][j] = min edits to transform s1[0:i] to s2[0:j].

**VARIANTS:**
- **4A: Return ops** — Return actual operations
- **4B: No replace** — Only insert/delete (no replace)
- **4C: Custom cost** — Each operation has different cost

**Interview Tip for Category 8:**  
DP is about:
1. **State definition** — DP[i] = answer for subproblem
2. **Transition** — How DP[i] depends on previous states
3. **Base case** — Starting conditions

---

# CATEGORY 9: DESIGN

## Core Pattern: Combine multiple data structures for O(1) operations
Use when: need multiple efficient operations (access, update, query) simultaneously.

### Problem 1: LRU Cache
**What it solves:** Cache with limited size, evict least recently used.

**BASE:**
```
LRUCache(2)
put(1, 1), put(2, 2), get(1)=1
put(3, 3) [evicts 2], get(2)=-1
Time: O(1) per operation, Space: O(capacity)
```
Structures: HashMap (O(1) access) + DoublyLinkedList (O(1) reorder).

**VARIANTS:**
- **1A: LFU Cache** — Evict least frequently used (more complex)
- **1B: TTL Cache** — Expire entries after time-to-live
- **1C: Multi-tier** — Hot cache (L1) + warm cache (L2)

### Problem 2: MinStack
**What it solves:** Stack with O(1) get_min().

**BASE:**
```
push(3), push(1), push(4)
top()=4, get_min()=1
Time: O(1) per operation, Space: O(n)
```
Strategy: Dual stack (values + minimums).

**VARIANTS:**
- **2A: MaxStack** — Also track maximum
- **2B: K-th largest** — Get K-th largest in stack
- **2C: Range queries** — Query min/max over indices [start, end]

### Problem 3: Union-Find
**What it solves:** Efficiently find & union elements into connected components.

**BASE:**
```
union(0, 1), union(2, 3)
connected(0, 1) = True, connected(0, 2) = False
Time: O(α(n)) amortized, Space: O(n)
```
Optimizations: Path compression + union by rank.

**VARIANTS:**
- **3A: Find components** — Return all connected components
- **3B: Cycle detection** — Use UF to detect cycles in graph
- **3C: Size tracking** — Know size of each component

### Problem 4: Median Finder
**What it solves:** Find median of stream (online).

**BASE:**
```
addNum(1), addNum(2), addNum(3)
findMedian() = 2
Time: O(log n) per addNum, O(1) for findMedian, Space: O(n)
```
Strategy: Two heaps (max-heap for left half, min-heap for right).

**VARIANTS:**
- **4A: K-th percentile** — K-th percentile instead of median
- **4B: Weighted median** — Percentiles with weights

---

# Interview Strategy

## Two-Step Recognition

### Step 1: Identify Core Pattern
Read problem → "This is Category X pattern"

- "Two numbers sum to target?" → Category 1 (Hashmap)
- "Longest substring / subarray?" → Category 2 (Sliding Window)
- "Palindrome / partition?" → Category 3 (Two Pointer)
- "Balanced / next-greater?" → Category 4 (Stack)
- "Sorted + find?" → Category 5 (Binary Search)
- "List manipulation / cycle?" → Category 6 (Linked List)
- "Tree traversal / islands?" → Category 7 (Tree/Graph)
- "Optimal count / min edits?" → Category 8 (DP)
- "Efficient cache / stream?" → Category 9 (Design)

### Step 2: Recognize Variant
Q1 (15 min): Solve base problem  
Q2 (45 min): "What if...?" → Recognize variant type:

| Variant Type | Question | Example |
|---|---|---|
| Output format | "Return count instead?" | Two Sum: return count of pairs |
| Constraint add | "Within distance K?" | Contains Duplicate: within K |
| Direction change | "From left instead?" | Next Greater: previous greater |
| Data structure | "Use 2-pointer instead?" | Two Sum sorted: no hashmap |
| Generalization | "3 numbers? 4? K?" | Two Sum → Three Sum → K-Sum |
| Condition flip | "Min instead of max?" | Container: min area |

### Step 3: Adapt Algorithm
Same core logic. Only change:
- What you track / output
- When to stop / continue
- Data structure choice

---

# Quick Reference by Difficulty

## Medium-Easy Q1 (Warm-up Level)
**Likely problems:**
- Two Sum (Category 1)
- Valid Parentheses (Category 4)
- Reverse Linked List (Category 6)
- Max Depth (Category 7)
- Climb Stairs (Category 8)

## Medium Q2 (Main Round)
**Likely problems + variant twist:**
- Longest Substring (Category 2) + variant
- Three Sum (Category 1/3) + custom target
- Shortest Window (Category 2) + exact constraint
- LRU Cache (Category 9) + LFU variant
- Coin Change (Category 8) + return coins

---

# File Structure

```
Category1_HashmapDict.py          [8 problems × 3-4 variants]
Category2_SlidingWindow.py        [6 problems × 3-4 variants]
Category3_TwoPointer.py           [6 problems × 3-4 variants]
Category4_Stack.py                [5 problems × 3-6 variants]
Category5_BinarySearch.py         [5 problems × 3-4 variants]
Category6_LinkedList.py           [5 problems × 3-4 variants]
Category7_TreeGraph.py            [4 problems × 3-4 variants]
Category8_DynamicProgramming.py  [4 problems × 3-4 variants]
Category9_Design.py               [4 problems × 3-4 variants]
```

Each file:
- ✅ Base problem with clear explanation
- ✅ 3-4 variants showing constraint adaptations
- ✅ Working code with test cases
- ✅ Complexity analysis
- ✅ Interview tips

---

# Pre-Interview Checklist

- [ ] Run all 9 category files to see output
- [ ] Understand core pattern for each category
- [ ] Code base problem for each category from memory
- [ ] Recognize at least 2 variants per category
- [ ] Practice variant adaptation (same logic, different output)
- [ ] Time yourself on base problems (should be <5 min each)

**You're ready when:** Interviewer says "what if we ..." and you think "that's variant X, which changes Y and Z, but core logic stays the same."

---

Good luck with Datadog! 🚀
