# Interview Prep with Variants — Complete Guide

## What's New

You now have **two levels** of problem files:

### **Level 1: Original Files (Categories 1-9)**
- `Category1_HashmapDict.py` through `Category9_Design.py`
- **What they contain:** Base problems with full explanations
- **Use when:** Learning the core pattern for the first time

### **Level 2: Variants Files (Categories 1-9)**
- `Category1_HashmapDict_WITH_VARIANTS.py` ✅ (Complete with 4 variants per problem)
- `Category2_SlidingWindow_WITH_VARIANTS.py` ✅ (Complete with 4 variants per problem)
- `VARIANTS_TEMPLATE.md` ✅ (Blueprint for Categories 3-9)

---

## How Variants Work

Each problem now shows:

1. **BASE Problem** — The foundation
   ```python
   def two_sum(numbers, target):
       # Find any pair summing to target
   ```

2. **VARIANT A** — Change output format
   ```python
   def count_pairs_summing_to(numbers, target):
       # Count pairs (not return them)
   ```

3. **VARIANT B** — Add constraints
   ```python
   def all_pairs_summing_to(numbers, target):
       # Return ALL pairs (not just one)
   ```

4. **VARIANT C** — Use different data structure
   ```python
   def two_sum_sorted(numbers, target):
       # Sorted array → two-pointer instead of hashmap
   ```

---

## The Variant Pattern Matrix

### **Variant Type 1: Output Format**
```
Boolean → Value → Count → All values
is_duplicate(arr)  →  first_duplicate(arr)  →  count_duplicates(arr)  →  all_duplicates(arr)
```

### **Variant Type 2: Constraints**
```
No limit → K limit → Exact value → Custom range
max_sum(arr)  →  max_sum_k(arr, k)  →  sum_equals(arr, target)  →  sum_in_range(arr, lo, hi)
```

### **Variant Type 3: Direction**
```
Forward → Backward → Both directions
next_greater  →  previous_greater  →  closest_greater
```

### **Variant Type 4: Aggregation**
```
Single best → All matching → Count
max_element  →  all_max_elements  →  count_max_elements
```

### **Variant Type 5: Data Structure**
```
Hashmap → Heap → Two-pointer → Sort
O(n) space  →  O(log n) space  →  O(1) space  →  O(n log n) time
```

### **Variant Type 6: Generalization**
```
2-Sum → 3-Sum → 4-Sum → K-Sum
O(n)  →  O(n²)  →  O(n³)  →  O(n^(k-1))
```

---

## How to Build Variants for Categories 3-9

### **Step 1: Pick a problem** (e.g., `Container With Most Water`)

### **Step 2: Create BASE solution**
```python
def max_area(heights):
    # Find max area between two lines
```

### **Step 3: Create 3-4 variants using the patterns above**

**VARIANT A** (Output change: max → min)
```python
def min_area(heights):
    # Find minimum area (same algorithm, flip comparison)
```

**VARIANT B** (Constraint change: single best → count)
```python
def count_pairs_area_k(heights, k):
    # How many pairs have area >= k?
```

**VARIANT C** (Generalization: 2 lines → 3 lines)
```python
def max_volume_3d(heights):
    # Max volume from 3 dimensions instead of 2
```

### **Step 4: Add explanations**
- What changes between variants
- Why this change affects the algorithm
- Time/space complexity for each

---

## Example: Build Variants for "Reverse Linked List" (Category 6)

```python
# BASE
def reverse_list(head):
    """Reverse entire list"""
    prev = None
    while current:
        next_tmp = current.next
        current.next = prev
        prev = current
        current = next_tmp
    return prev

# VARIANT A: Reverse only first K nodes
def reverse_first_k(head, k):
    """Same algorithm, but stop after K nodes"""
    # Pointer manipulation + counter (stop at k)
    
# VARIANT B: Reverse in groups of K
def reverse_k_nodes(head, k):
    """Reverse every K nodes: [a,b,c,d,e], k=2 → [b,a,d,c,e]"""
    # Outer loop + reverse each group + reconnect groups
    
# VARIANT C: Reverse between M and N
def reverse_between(head, m, n):
    """Reverse only nodes from position M to N"""
    # Pointer tracking + partial reversal + rejoining
```

**The Core Insight:** All variants use the same **core pointer manipulation**. Only the **starting point**, **stopping point**, and **how to reconnect** change.

---

## Interview Strategy Using Variants

### **When you see a problem in an interview:**

1. **Identify the core pattern**
   - Is it a Two Pointer problem? Hashmap? DP?
   
2. **Ask yourself: Is this a variant?**
   - Does it ask for count instead of value? → Variant Type 1
   - Does it add a constraint (K limit, distance, etc.)? → Variant Type 2
   - Does it generalize (2-sum → 3-sum)? → Variant Type 6

3. **Adapt the base algorithm**
   - The core logic stays the same
   - Only the output, constraint, or data structure changes

4. **Implement with confidence**
   - You've already seen this pattern before
   - It's just a variant of something you know

### **Example Live Interview:**

**Interviewer:** "You'll solve Two Sum. First the base problem, then we'll add variants."

**You (mentally):** "Ok, base is hashmap check-and-remember. Let me think about variants:
- Count pairs? → Track count instead of returning
- All pairs? → Use a set of pairs, not early return
- Sorted array? → Two pointers, O(1) space
- Three sum? → Outer loop + two-pointer on remainder
"

**You (out loud):** "I can solve the base in O(n) time. For variants, I'd count pairs, return all pairs, or switch to two-pointer for sorted input. Should I code one or talk through all?"

---

## Next Steps

### **To Complete Categories 3-9 Variants:**

1. **Read** `VARIANTS_TEMPLATE.md` to understand the variants for each category
2. **Pick a category** (e.g., Category 3: Two Pointer)
3. **Implement 2-3 variants** for each problem using the patterns above
4. **Test each variant** (run the code, verify output)
5. **Add explanations** (what changed, why it matters)

### **Practice Flow:**

Day 1: Master Category 1 + variants (you've got this with the WITH_VARIANTS file)
Day 2: Category 2 + variants (WITH_VARIANTS file ready)
Day 3-9: Apply template to remaining categories + implement variants

---

## Files in Your Folder

```
✅ Category1_HashmapDict.py (base)
✅ Category1_HashmapDict_WITH_VARIANTS.py (complete!)
✅ Category2_SlidingWindow.py (base)
✅ Category2_SlidingWindow_WITH_VARIANTS.py (complete!)
✅ Category3_TwoPointer.py through Category9_Design.py (base only)
📋 VARIANTS_TEMPLATE.md (blueprint for 3-9)
📖 README_Categories.md (original structure guide)
📖 README_VARIANTS.md (THIS FILE)
```

---

## Why Variants Matter for Datadog Interviews

Datadog's interview pattern:
1. **Q1 (15 min):** Base problem (medium easy)
2. **Follow-up (45 min):** Variant with constraint twist

When you master variants, you've basically **pre-answered their follow-ups**. You won't be caught off-guard by "what if we add this constraint?"

---

## Good luck! 🚀

You now have the most powerful framework for interview prep:
- **Core patterns** (9 categories)
- **Variants** (6 types of constraints)
- **Strategy** (recognize core → adapt to variant)

Every "new" problem is just a variant of something you've already solved.
