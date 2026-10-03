# ============================================================
# Category 4: Stack Problems
# Core pattern: LIFO + pattern matching or monotonic stack
# ============================================================

from collections import deque

# PROBLEM 1: Valid Parentheses
# QUESTION: Check if brackets are balanced and in correct order: (), [], {}
# EXPLANATION: Push openers to stack, pop and match on closers. If no match or stack empty, invalid.
# WHY: Stack is perfect for nested matching (LIFO ensures inner closes before outer).
# TIME/SPACE: O(n) time, O(n) space

def is_valid_parentheses(s):
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack

print("is_valid_parentheses('({[]})'):", is_valid_parentheses('({[]})'))
print()


# PROBLEM 2: Remove Adjacent Duplicates
# QUESTION: Collapse adjacent matching characters. E.g., "abbaca" → "ca" (b's collapse, then a's)
# EXPLANATION: Stack acts as a string builder. If top == current, pop (they cancel). Else push.
# KEY: The result grows/shrinks as you process, which is why stack fits perfectly.
# TIME/SPACE: O(n) time, O(n) space

def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

print("remove_adjacent_duplicates('abbaca'):", remove_adjacent_duplicates('abbaca'))
print()


# PROBLEM 3: MinStack
# QUESTION: Design a stack that supports push, pop, top, and get_min() in O(1)
# EXPLANATION: Use TWO stacks: main stack for values, min_stack for minimums seen so far.
# When pushing, also push to min_stack if it's the new minimum.
# When popping, pop from min_stack if the value being removed was the minimum.
# WHY: Dual tracking lets you keep O(1) minimum at all times.
# TIME/SPACE: O(1) per operation, O(n) space

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
print("MinStack: top =", ms.top(), ", min =", ms.get_min())
print()


# PROBLEM 4: Next Greater Element
# QUESTION: For each element, find the next element to its right that's larger. Return array of answers.
# EXPLANATION: Use MONOTONIC STACK (stack of indices in decreasing order of values).
# Walk RIGHT to LEFT. When current is larger than stack top, we found "next greater" for stack top.
# WHY: Monotonic invariant lets us match elements efficiently without nested loops.
# TIME/SPACE: O(n) time (each element pushed/popped once), O(n) space

def next_greater_element(numbers):
    result = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(numbers[i])
    return result

print("next_greater_element([1, 3, 2, 4]):", next_greater_element([1, 3, 2, 4]))
print()


# PROBLEM 5: Daily Temperatures
# QUESTION: For each day, find how many days until a warmer day. Use stack of indices.
# EXPLANATION: Process left-to-right. Use monotonic stack of temps (decreasing).
# When current temp > stack top, we found "next warmer" for stack top day.
# Store the distance (current_index - stack_top_index).
# WHY: Same monotonic idea as Problem 4, but tracking distances and modifying stack differently.
# TIME/SPACE: O(n) time, O(n) space

def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            result[stack.pop()] = i - stack[-1]
        stack.append(i)
    return result

print("daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]):", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print()


# PROBLEM 6: Decode String
# QUESTION: Decode a string with pattern "num[str]", e.g., "3[a2[c]]" → "acaca"
# EXPLANATION: Use stack to handle nested brackets. When hitting ']', pop to decode innermost.
# Push digits and strings back onto stack. At end, stack contains the decoded string.
# GOTCHA: Need to handle multi-digit numbers.
# TIME/SPACE: O(n) time (where n is length of decoded string, could be exponential), O(stack size)

def decode_string(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = []
            while stack and stack[-1] != '[':
                substr.insert(0, stack.pop())
            stack.pop()  # remove '['
            num_str = []
            while stack and stack[-1].isdigit():
                num_str.insert(0, stack.pop())
            num = int(''.join(num_str)) if num_str else 1
            decoded = ''.join(substr) * num
            for c in decoded:
                stack.append(c)
    return ''.join(stack)

print("decode_string('3[a2[c]]'):", decode_string('3[a2[c]]'))
print()


# PROBLEM 7: Largest Rectangle in Histogram
# QUESTION: Given heights, find largest rectangular area possible in histogram
# EXPLANATION: Use monotonic stack of indices (in increasing height order).
# When current height < stack top, pop and calculate area with popped height as the height.
# WHY: Monotonic stack avoids nested loops while tracking valid rectangles.
# TIME/SPACE: O(n) time, O(n) space

def largest_rectangle(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            w = i if not stack else i - stack[-1] - 1
            area = heights[top] * w
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        area = heights[top] * w
        max_area = max(max_area, area)
    return max_area

print("largest_rectangle([2, 1, 5, 6, 2, 3]):", largest_rectangle([2, 1, 5, 6, 2, 3]))
print()


# PROBLEM 8: Simplify Path
# QUESTION: Given a Unix path, simplify it (resolve . and .. navigations)
# EXPLANATION: Stack stores directory names. Process path parts:
#   - "." → skip (current directory)
#   - ".." → pop if stack not empty (go to parent)
#   - anything else → push (enter directory)
# WHY: Stack naturally models directory hierarchy (can push and pop).
# TIME/SPACE: O(n) time, O(n) space

def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part and part != '.' and part != '..':
            stack.append(part)
        elif part == '..' and stack:
            stack.pop()
    return '/' + '/'.join(stack)

print("simplify_path('/a/./b/../../c/'):", simplify_path('/a/./b/../../c/'))
