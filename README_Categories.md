# SWE Internship Interview Prep — 9 Categories

All files are complete with solutions. Each file is runnable directly:

```bash
python Category1_HashmapDict.py
python Category2_SlidingWindow.py
# ... etc
```

---

## Category 1: Hashmap / Dict Problems
**File:** `Category1_HashmapDict.py`

- **Core pattern:** "check + remember" via dict/set
- **Problems:** 10 total
  - `two_sum` — foundation
  - `contains_duplicate`, `is_anagram` — membership checks
  - `group_anagrams` — grouping by key
  - `count_all`, `most_frequent`, `least_frequent` — frequency counting
  - `has_pair_summing_to`, `common_elements` — set operations
  - `two_sum_sorted` — **MIXED: hashmap + two-pointer**

**Datadog likelihood:** Very high (all patterns)

---

## Category 2: Sliding Window
**File:** `Category2_SlidingWindow.py`

- **Core pattern:** Fixed/variable window, maintain state between expansions
- **Problems:** 8 total
  - `max_sum_subarray` — fixed window
  - `max_profit` — min/max tracking
  - `length_of_longest_substring` — variable window with uniqueness
  - `longest_substring_k_distinct` — at-most-k distinct
  - `shortest_burst` — at-least-threshold sum
  - `min_window_substring` — **MIXED: sliding window + hashmap**
  - `longest_repeating_char` — replace-with-budget
  - `is_valid_palindrome_substring` — window of fixed size

**Datadog likelihood:** High (Question 2 from MockTest)

---

## Category 3: Two Pointer
**File:** `Category3_TwoPointer.py`

- **Core pattern:** Pointers from both ends or running alongside
- **Problems:** 8 total
  - `is_palindrome` — standard palindrome
  - `max_area` — water container
  - `three_sum` — triplets with target
  - `remove_duplicates_sorted` — in-place removal
  - `is_sorted_rotated` — rotation detection
  - `two_sum_sorted_array` — **MIXED: two-pointer on sorted**
  - `partition_colors` — Dutch flag (three-way)
  - `trapping_rain_water` — rainwater collection

**Datadog likelihood:** Medium-high (paired with sorted/array constraints)

---

## Category 4: Stack
**File:** `Category4_Stack.py`

- **Core pattern:** LIFO matching, monotonic stack tricks
- **Problems:** 8 total
  - `is_valid_parentheses` — bracket matching
  - `remove_adjacent_duplicates` — stack as collector
  - `MinStack` class — O(1) min retrieval
  - `next_greater_element` — monotonic stack
  - `daily_temperatures` — next greater with indices
  - `decode_string` — **MIXED: stack + string parsing**
  - `largest_rectangle` — monotonic stack pattern
  - `simplify_path` — stack for path traversal

**Datadog likelihood:** Medium (especially monotonic stack variants)

---

## Category 5: Binary Search
**File:** `Category5_BinarySearch.py`

- **Core pattern:** O(log n) on sorted/structured data
- **Problems:** 8 total
  - `binary_search` — standard
  - `first_position_of` — leftmost boundary
  - `search_rotated_sorted` — rotated array
  - `find_peak` — peak finding
  - `sqrt_int` — floating-point analog
  - `min_rotated` — **MIXED: binary search + validation**
  - `find_insert_position` — insertion point
  - `capacity_to_ship_packages` — **MIXED: binary search + feasibility check**

**Datadog likelihood:** Medium (less common than hashmap/sliding, but guaranteed to appear)

---

## Category 6: Linked List
**File:** `Category6_LinkedList.py`

- **Core pattern:** Pointer manipulation, two-pointer, cycle detection
- **Problems:** 8 total
  - `reverse_list` — basic reversal
  - `merge_two_lists` — merging sorted lists
  - `has_cycle` — slow/fast pointers
  - `find_middle` — slow/fast for middle
  - `remove_nth_from_end` — dummy node pattern
  - `is_palindrome_list` — **MIXED: linked list + two-pointer + reversal**
  - `reorder_list` — reorder via split/reverse/merge
  - `build_list` / `print_list` — utility functions

**Datadog likelihood:** Medium (less frequent than arrays, but core skill)

---

## Category 7: Tree / Graph
**File:** `Category7_TreeGraph.py`

- **Core pattern:** BFS/DFS, recursion, visited tracking
- **Problems:** 8 total
  - `max_depth_tree` — depth via recursion
  - `level_order_traversal` — BFS
  - `is_valid_bst` — BST validation
  - `num_islands` — grid DFS
  - `has_path_graph` — graph traversal
  - `inorder_traversal` — **MIXED: tree + list-building**
  - `path_sum` — path-based recursion
  - `lowest_common_ancestor` — LCA

**Datadog likelihood:** Medium-high (graphs especially for distributed systems interviews)

---

## Category 8: Dynamic Programming
**File:** `Category8_DynamicProgramming.py`

- **Core pattern:** Memoization, table building, state transitions
- **Problems:** 9 total
  - `climb_stairs` — base recurrence
  - `fib_memo` — memoization template
  - `max_subarray` — Kadane's algorithm
  - `coin_change` — min coins
  - `coin_change_ways` — count ways
  - `longest_common_subsequence` — 2D DP
  - `edit_distance` — Levenshtein
  - `longest_increasing_subsequence` — LIS
  - `knapsack_01` — **MIXED: DP + resource constraint**

**Datadog likelihood:** Medium (often as a "gotcha" second part of a problem)

---

## Category 9: Design
**File:** `Category9_Design.py`

- **Core pattern:** Combine data structures for O(1) operations
- **Problems:** 7 total (classes/systems)
  - `LRUCache` — dict + OrderedDict
  - `MinStack` — dual stacks
  - `LFUCache` — dict + defaultdict of OrderedDicts
  - `RandomizedSet` — dict + list
  - `UnionFind` — find/union with path compression
  - `MedianFinder` — dual heaps
  - `TimeBasedKeyValueStore` — **MIXED: design + binary search**

**Datadog likelihood:** Medium (LRU especially; full LFU is harder)

---

## Cross-Category ("Mixed") Problems

Problems tagged **MIXED** combine techniques from multiple categories:

1. **Two Sum (Sorted)** — Category 1 + Category 3 (two-pointer variant of hashmap idea)
2. **Min Window Substring** — Category 2 + Category 1 (sliding window with hashmap state)
3. **Two Sum (Sorted Array)** — Category 5 + Category 3 (binary search + two-pointer on sorted)
4. **Capacity to Ship** — Category 5 + feasibility check (binary search + validation)
5. **Is Palindrome (Linked List)** — Category 6 + Category 3 + reversal (two-pointer on list)
6. **Inorder Traversal** — Category 7 + list-building (tree + accumulator)
7. **Knapsack** — Category 8 + resource constraint logic (DP + bounded optimization)
8. **Time-Based KV Store** — Category 9 + binary search (design + search)
9. **Largest Rectangle** — Category 4 + monotonic reasoning (stack + geometry)
10. **Decode String** — Category 4 + string parsing (stack + character handling)

**Why mixed problems matter:** Datadog often asks a simple problem, then adds: "What if the input is also sorted?" or "And it needs to be in O(1) space," forcing you to shift strategies mid-interview.

---

## Recommended Practice Order

1. **Start here** (highest ROI for Datadog):
   - Category 1: Hashmap (especially `two_sum`, `has_pair_summing_to`)
   - Category 2: Sliding Window (Question 2 pattern)
   - Category 4: Stack (e.g., `is_valid_parentheses`)

2. **Next** (solidify fundamentals):
   - Category 3: Two Pointer (especially `three_sum`, `max_area`)
   - Category 5: Binary Search (unexpected in "easy" rounds, but classic)

3. **Strengthen depth**:
   - Category 6: Linked List (`merge_two_lists`, `has_cycle`)
   - Category 7: Tree/Graph (BFS/DFS comfort)

4. **Polish for hard rounds**:
   - Category 8: DP (`coin_change`, `edit_distance`)
   - Category 9: Design (`LRUCache`, `MinStack`)

---

## Running Tests

Each file is self-contained and prints test output:

```bash
python Category1_HashmapDict.py
# Output: two_sum([2, 7, 11, 15], 9): [7, 2]
#         contains_duplicate([1, 2, 3, 2]): True
#         ...etc
```

All solutions include **Big-O annotations** and are verified working.

---

## For Datadog Specifically

Based on recent patterns from Glassdoor/LeetCode:

- **Q1 (15 min easy-medium):** Usually Category 1 or 3 (hashmap/two-pointer)
- **Q2 (45 min medium):** Usually Category 2 (sliding window) or Category 5 (binary search)
- **Behavioral:** Leadership principles, debugging approach, team fit
- **Follow-up:** "What if input is 10GB?" → space/time tradeoff discussion

Good luck! 🚀
