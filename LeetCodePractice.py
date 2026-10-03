# ============================================================
# LeetCode practice, organized by pattern (not raw difficulty).
# Grouped this way on purpose: recognizing "this is a sliding-window
# problem" transfers to problems you've never seen. Difficulty is
# tagged per problem so you still know what you're looking at.
#
# How to use each one:
#   1. Read the problem.
#   2. Before writing any code, fill in the "Approach" comment in
#      your own words -- what's the algorithm, and why does it work?
#      Ask me to explain it if you want to understand it before you
#      attempt it yourself -- that's the whole point of doing this step.
#   3. Then write the code in the function below it.
#   4. Add a Big-O time/space comment once it's working, same as
#      every other file in this folder.
#
# This is a starting set -- ask for more in any category, or a new
# category entirely, whenever you're ready.
# ============================================================


# ---- Category: Arrays & Hashmaps ----

"""Two Sum (LeetCode 1, Easy)
Given a list of numbers and a target, return the two numbers that add
up to the target. Assume exactly one valid pair exists.

Approach:
1. Create an empty set called `seen`, to hold every number already looked at.
2. Loop through the numbers one at a time. For the CURRENT number:
   a. Compute `needed = target - current number` -- the value that would
      complete a pair with this one.
   b. Check: is `needed` already in `seen`? If yes, we've found the pair
      -- return [needed, current number].
   c. Remember: add the current number to `seen`, then move to the next.
3. If the loop finishes with no match, no valid pair exists.

"""
def two_sum(numbers, target):
    seen = {}
    for number in numbers:
        needed = target - number
        if needed in seen:
            return [needed, number]
        seen[number] = True
    return None
print('two_sum:', two_sum([2, 7, 11, 15], 9))


"""Contains Duplicate (LeetCode 217, Easy)
Given a list of numbers, return True if any value appears more than
once, False if every value is unique.

Approach:
1. create an empty set called 'seen', to hold every number already looked at
2. loop through the numbers one at a time. For the current number:
    a. check whether that number already exists in the seen set, if yes, print True
    b. if no, print false


"""
def contains_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False
    


"""Valid Anagram (LeetCode 242, Easy)
Given two strings, return True if the second is an anagram of the
first (same letters, same counts, any order).

Approach:
1. create an empty set called 'counts'


"""
def is_anagram(s, t):
    counts = {}
    pass


"""Group Anagrams (LeetCode 49, Medium)
Given a list of strings, group the ones that are anagrams of each
other together. Return the groups (order of groups doesn't matter).

Approach:


"""
def group_anagrams(words):
    pass


"""Top K Frequent Elements (LeetCode 347, Medium)
Given a list of numbers and an integer k, return the k most frequent
numbers in the list.

Approach:


"""
def top_k_frequent(numbers, k):
    pass


"""Product of Array Except Self (LeetCode 238, Medium)
Given a list of numbers, return a new list where each position holds
the product of every number EXCEPT the one at that position -- and
you can't use division.

Approach:


"""
def product_except_self(numbers):
    pass


# ---- Category: Sliding window ----

"""Best Time to Buy and Sell Stock (LeetCode 121, Easy)
Given a list of daily stock prices, find the maximum profit from
buying on one day and selling on a later day. Return 0 if no profit
is possible.

Approach:


"""
def max_profit(prices):
    pass


"""Longest Substring Without Repeating Characters (LeetCode 3, Medium)
Given a string, find the length of the longest substring that has no
repeated characters.

Approach:


"""
def length_of_longest_substring(s):
    pass


# ---- Category: Two pointers ----

"""Valid Palindrome (LeetCode 125, Easy)
Given a string, return True if it reads the same forwards and
backwards, ignoring case and ignoring anything that isn't a letter
or number.

Approach:


"""
def is_palindrome(s):
    pass


"""Container With Most Water (LeetCode 11, Medium)
Given a list of heights (each one a vertical line at that index),
find the two lines that, together with the x-axis, form the
container holding the most water. Return the max area.

Approach:


"""
def max_area(heights):
    pass


"""3Sum (LeetCode 15, Medium)
Given a list of numbers, find all unique triplets that add up to 0.
Return the triplets (no duplicates).

Approach:


"""
def three_sum(numbers):
    pass


# ---- Category: Stacks ----

"""Valid Parentheses (LeetCode 20, Easy)
Given a string of just '(', ')', '{', '}', '[', ']', return True if
every bracket is closed in the right order.

Approach:


"""
def is_valid_parentheses(s):
    pass


"""Min Stack (LeetCode 155, Medium)
Design a stack that supports push, pop, top, and retrieving the
minimum element, all in O(1).

Approach:


"""
class MinStack:
    def __init__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass


# ---- Category: Binary search ----

"""Binary Search (LeetCode 704, Easy)
Given a sorted list of numbers and a target, return the target's
index, or -1 if it isn't present.

Approach:


"""
def binary_search(numbers, target):
    pass


"""Search in Rotated Sorted Array (LeetCode 33, Medium)
A sorted list has been rotated at some unknown pivot (e.g. [4,5,6,7,0,1,2]
was [0,1,2,4,5,6,7] rotated). Given the rotated list and a target,
find the target's index in O(log n), or -1 if it isn't present.

Approach:


"""
def search_rotated(numbers, target):
    pass


# ---- Category: Linked lists ----

"""Reverse Linked List (LeetCode 206, Easy)
Given the head of a singly linked list, reverse it and return the
new head.

Approach:


"""
def reverse_list(head):
    pass


"""Merge Two Sorted Lists (LeetCode 21, Easy)
Given the heads of two sorted linked lists, merge them into one
sorted linked list and return its head.

Approach:


"""
def merge_two_lists(list1, list2):
    pass


"""Linked List Cycle (LeetCode 141, Easy)
Given the head of a linked list, return True if it contains a cycle
(some node's `next` eventually points back to an earlier node).

Approach:


"""
def has_cycle(head):
    pass


# ---- Category: Trees / BFS / DFS ----

"""Maximum Depth of Binary Tree (LeetCode 104, Easy)
Given the root of a binary tree, return its depth (the number of
nodes along the longest path from root to a leaf).

Approach:


"""
def max_depth(root):
    pass


"""Binary Tree Level Order Traversal (LeetCode 102, Medium)
Given the root of a binary tree, return its values grouped level by
level (a list of lists), top to bottom.

Approach:


"""
def level_order(root):
    pass


"""Validate Binary Search Tree (LeetCode 98, Medium)
Given the root of a binary tree, return True if it's a valid binary
search tree (every left descendant < node < every right descendant,
for every node -- not just each node's direct children).

Approach:


"""
def is_valid_bst(root):
    pass


# ---- Category: Graphs ----

"""Number of Islands (LeetCode 200, Medium)
Given a 2D grid of '1' (land) and '0' (water), count the number of
islands. An island is formed by connecting adjacent land cells
horizontally or vertically.

Approach:


"""
def num_islands(grid):
    pass


"""Clone Graph (LeetCode 133, Medium)
Given a reference to a node in a connected undirected graph, return a
deep copy (clone) of the entire graph.

Approach:


"""
def clone_graph(node):
    pass


# ---- Category: Dynamic programming (basic) ----

"""Climbing Stairs (LeetCode 70, Easy)
You're climbing a staircase with n steps. You can climb 1 or 2 steps
at a time. How many distinct ways can you reach the top?

Approach:


"""
def climb_stairs(n):
    pass


"""Maximum Subarray (LeetCode 53, Medium)
Given a list of numbers, find the contiguous subarray with the
largest sum, and return that sum.

Approach:


"""
def max_subarray(numbers):
    pass


"""Coin Change (LeetCode 322, Medium)
Given a list of coin denominations and a target amount, return the
FEWEST number of coins needed to make that amount. Return -1 if it
can't be made.

Approach:


"""
def coin_change(coins, amount):
    pass


# ---- Category: Design ----

"""LRU Cache (LeetCode 146, Medium)
Design a fixed-capacity cache that evicts the least recently used
item when it's full. Both get and put should run in O(1).

Approach:


"""
class LRUCache:
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass
