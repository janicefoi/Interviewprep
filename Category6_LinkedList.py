# ============================================================
# Category 6: Linked List Problems
# Core pattern: pointer manipulation, traversal, two-pointer
# ============================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    print(" -> ".join(map(str, result)))
    return result


# O(n) time, O(1) space
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_tmp = current.next
        current.next = prev
        prev = current
        current = next_tmp
    return prev

head = build_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)
print("reverse_list([1,2,3,4,5]):", print_list(reversed_head))


# O(n) time, O(1) space
def merge_two_lists(list1, list2):
    dummy = Node(0)
    current = dummy
    p1, p2 = list1, list2
    while p1 and p2:
        if p1.value <= p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    current.next = p1 or p2
    return dummy.next

l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
merged = merge_two_lists(l1, l2)
print("merge_two_lists([1,2,4], [1,3,4]):", print_list(merged))


# O(n) time, O(1) space
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test: create a cycle
head_cycle = build_list([3, 2, 0, -4])
head_cycle.next.next.next.next = head_cycle.next  # create cycle
print("has_cycle (with cycle):", has_cycle(head_cycle))


# O(n) time, O(1) space
def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = build_list([1, 2, 3, 4, 5])
middle = find_middle(head)
print("find_middle([1,2,3,4,5]):", middle.value if middle else None)


# O(n) time, O(1) space
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        if first:
            first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

head = build_list([1, 2, 3, 4, 5])
result = remove_nth_from_end(head, 2)
print("remove_nth_from_end([1,2,3,4,5], 2):", print_list(result))


# O(n) time, O(1) space  [MIXED: linked list + two-pointer]
def is_palindrome_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = reverse_list(slow)
    first = head
    while second:
        if first.value != second.value:
            return False
        first = first.next
        second = second.next
    return True

head = build_list([1, 2, 2, 1])
print("is_palindrome_list([1,2,2,1]):", is_palindrome_list(head))


# O(n) time, O(1) space
def reorder_list(head):
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = reverse_list(slow)
    first = head
    while second.next:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

head = build_list([1, 2, 3, 4])
reorder_list(head)
print("reorder_list([1,2,3,4]):", print_list(head))
