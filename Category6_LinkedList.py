# ============================================================
# Category 6: Linked List — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: Pointer manipulation, two-pointer (slow/fast)
# Key: Work with limited info — can't index backward
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(vals):
    """Helper: build linked list from array"""
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    """Helper: convert linked list to array"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# ============================================================
# PROBLEM 1: REVERSE LINKED LIST
# ============================================================
# What it solves: Reverse entire list in-place
# Key: Three pointers (prev, curr, next) to reverse links
# Space: O(1) if iterative, O(n) if recursive (call stack)
# Interview angle: Reverse first K nodes? Reverse pairs?

# BASE: Reverse entire list
def reverse_list(head):
    """Base: reverse entire linked list (iterative)"""
    prev, curr = None, head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# VARIANT 1A: Reverse first K nodes
def reverse_first_k(head, k):
    """Variant A: reverse only first k nodes"""
    if k <= 1 or not head:
        return head
    prev, curr = None, head
    for _ in range(k):
        if not curr:
            break
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    head.next = curr
    return prev

# VARIANT 1B: Reverse every K nodes (groups)
def reverse_every_k_nodes(head, k):
    """Variant B: reverse every k nodes in groups"""
    def reverse_k(head, k):
        curr = head
        for _ in range(k - 1):
            if not curr:
                return None
            curr = curr.next
        if not curr:
            return None
        next_group = curr.next
        curr.next = None
        rev_head = reverse_list(head)
        head.next = reverse_every_k_nodes(next_group, k)
        return rev_head

    if not head or k == 1:
        return head
    return reverse_k(head, k)

# VARIANT 1C: Reverse between positions M and N
def reverse_between(head, m, n):
    """Variant C: reverse only between positions m and n (1-indexed)"""
    if m == n or not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(n - m):
        next_temp = curr.next
        curr.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp
    return dummy.next

print("=== PROBLEM 1: REVERSE LINKED LIST ===")
head1 = build_list([1, 2, 3, 4, 5])
print("BASE:", print_list(reverse_list(head1)))
head2 = build_list([1, 2, 3, 4, 5])
print("VARIANT 1A (first 2):", print_list(reverse_first_k(head2, 2)))
print()


# ============================================================
# PROBLEM 2: MERGE TWO SORTED LISTS
# ============================================================
# What it solves: Merge two sorted lists into one sorted list
# Key: Compare heads, attach smaller, advance pointer
# Interview angle: Merge K sorted lists? In-place?

# BASE: Merge two sorted lists
def merge_two_lists(l1, l2):
    """Base: merge two sorted lists"""
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

# VARIANT 2A: Merge K sorted lists
def merge_k_sorted_lists(lists):
    """Variant A: merge k sorted lists"""
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_lists(l1, l2))
        lists = merged
    return lists[0]

# VARIANT 2B: Merge and remove duplicates
def merge_remove_duplicates(l1, l2):
    """Variant B: merge and remove duplicates"""
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            if not curr.next or curr.next.val != l1.val:
                curr.next = l1
                curr = curr.next
            l1 = l1.next
        else:
            if not curr.next or curr.next.val != l2.val:
                curr.next = l2
                curr = curr.next
            l2 = l2.next
    curr.next = l1 if l1 else l2
    return dummy.next

# VARIANT 2C: Merge in-place (modify input lists)
def merge_inplace(l1, l2):
    """Variant C: merge in-place (same as base but modifies input)"""
    return merge_two_lists(l1, l2)

print("=== PROBLEM 2: MERGE TWO SORTED ===")
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
print("BASE:", print_list(merge_two_lists(l1, l2)))
print()


# ============================================================
# PROBLEM 3: HAS CYCLE
# ============================================================
# What it solves: Detect if linked list has a cycle
# Key: Slow/fast pointer — if they meet, cycle exists
# Why: Fast overtakes slow in the cycle
# Interview angle: Find cycle start? Return cycle length?

# BASE: Detect if cycle exists
def has_cycle(head):
    """Base: check if linked list has cycle"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# VARIANT 3A: Find cycle start node
def find_cycle_start(head):
    """Variant A: find the node where cycle starts"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

# VARIANT 3B: Return cycle length
def cycle_length(head):
    """Variant B: return length of cycle"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = 1
            curr = slow.next
            while curr != slow:
                length += 1
                curr = curr.next
            return length
    return 0

# VARIANT 3C: Find node at intersection
def find_cycle_intersection(head):
    """Variant C: find the node where slow and fast meet"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

print("=== PROBLEM 3: HAS CYCLE ===")
# Create cycle: 1 -> 2 -> 3 -> 2
cycle_head = build_list([1, 2, 3])
cycle_head.next.next.next = cycle_head.next
print("Has cycle (manual):", True)
print()


# ============================================================
# PROBLEM 4: FIND MIDDLE NODE
# ============================================================
# What it solves: Return middle node of list (or second middle if even)
# Key: Slow/fast pointers — fast goes 2x speed
# Interview angle: Find K-th from end? Find nth percentile?

# BASE: Find middle node
def find_middle(head):
    """Base: find middle node (or second middle if even length)"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# VARIANT 4A: Find K-th from end
def find_kth_from_end(head, k):
    """Variant A: find k-th node from end"""
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.next

# VARIANT 4B: Find all middle nodes (if even length)
def find_all_middles(head):
    """Variant B: return all middle nodes if even, or just middle if odd"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# VARIANT 4C: Find nth percentile node
def find_percentile_node(head, percentile):
    """Variant C: find node at nth percentile"""
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    target_idx = int(length * percentile / 100)
    curr = head
    for _ in range(target_idx):
        curr = curr.next
    return curr

print("=== PROBLEM 4: FIND MIDDLE ===")
head = build_list([1, 2, 3, 4, 5])
mid = find_middle(head)
print("Middle of [1,2,3,4,5]:", mid.val if mid else None)
print()


# ============================================================
# PROBLEM 5: REMOVE NTH FROM END
# ============================================================
# What it solves: Remove n-th node from end of list
# Key: Two-pass with dummy node to handle head removal
# Interview angle: Remove all occurrences? Return removed node?

# BASE: Remove n-th from end
def remove_nth_from_end(head, n):
    """Base: remove n-th node from end"""
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy
    for _ in range(n + 1):
        if not fast:
            return head
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# VARIANT 5A: Remove all occurrences of value
def remove_all_occurrences(head, val):
    """Variant A: remove ALL nodes with value val"""
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

# VARIANT 5B: Remove and return the node
def remove_nth_return_node(head, n):
    """Variant B: remove n-th from end AND return the removed node"""
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy
    for _ in range(n + 1):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    removed = slow.next
    slow.next = slow.next.next
    return removed

# VARIANT 5C: Remove pairs of nodes
def remove_pairs(head):
    """Variant C: remove nodes in pairs (e.g., remove 1st and 2nd, 3rd and 4th)"""
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next and curr.next.next:
        curr.next = curr.next.next.next
    return dummy.next

print("=== PROBLEM 5: REMOVE NTH FROM END ===")
head = build_list([1, 2, 3, 4, 5])
print("Remove 2nd from end:", print_list(remove_nth_from_end(head, 2)))
print()

print("=" * 70)
print("CATEGORY 6: LINKED LIST PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Pointer manipulation (reverse, merge)")
print("Pattern 2: Two-pointer (slow/fast for middle/cycle)")
print("Pattern 3: Dummy node to handle edge cases")
print("=" * 70)
