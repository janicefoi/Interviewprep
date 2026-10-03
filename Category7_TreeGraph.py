# ============================================================
# Category 7: Tree / Graph — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: BFS/DFS, recursion, traversal
# Key: Choose traversal based on problem (level-order vs depth-first)
# ============================================================

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM 1: MAX DEPTH (HEIGHT OF TREE)
# ============================================================
# What it solves: Find height of binary tree (max levels from root to leaf)
# Recursive: max(left_depth, right_depth) + 1
# Iterative: BFS level by level
# Interview angle: Min depth? Path with max depth?

# BASE: Maximum depth (height)
def max_depth_tree(root):
    """Base: find maximum depth (height) of binary tree"""
    if not root:
        return 0
    return 1 + max(max_depth_tree(root.left), max_depth_tree(root.right))

# VARIANT 1A: Minimum depth
def min_depth_tree(root):
    """Variant A: minimum depth (shortest path to leaf)"""
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth_tree(root.right)
    if not root.right:
        return 1 + min_depth_tree(root.left)
    return 1 + min(min_depth_tree(root.left), min_depth_tree(root.right))

# VARIANT 1B: Count nodes at max depth
def count_max_depth_nodes(root):
    """Variant B: count how many nodes are at maximum depth"""
    def helper(node):
        if not node:
            return 0, 0
        if not node.left and not node.right:
            return 1, 1
        left_depth, left_count = helper(node.left)
        right_depth, right_count = helper(node.right)
        max_d = max(left_depth, right_depth) + 1
        count = left_count if left_depth > right_depth else (right_count if right_depth > left_depth else left_count + right_count)
        return max_d, count
    return helper(root)[1]

# VARIANT 1C: Path to deepest node
def path_to_deepest_node(root):
    """Variant C: return path (list of values) to deepest node"""
    def helper(node):
        if not node:
            return [], 0
        if not node.left and not node.right:
            return [node.val], 1
        left_path, left_depth = helper(node.left)
        right_path, right_depth = helper(node.right)
        if left_depth > right_depth:
            return [node.val] + left_path, left_depth + 1
        else:
            return [node.val] + right_path, right_depth + 1
    return helper(root)[0]

print("=== PROBLEM 1: MAX DEPTH ===")
# Example tree: 3, 9, 20, null, null, 15, 7
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
print("Max depth:", max_depth_tree(tree))
print("Min depth:", min_depth_tree(tree))
print()


# ============================================================
# PROBLEM 2: LEVEL ORDER TRAVERSAL
# ============================================================
# What it solves: Return nodes grouped by level (BFS)
# Key: Use queue, process level by level
# Interview angle: Reverse levels? Zigzag? Rightmost per level?

# BASE: Level order (return levels)
def level_order_traversal(root):
    """Base: return nodes grouped by level"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# VARIANT 2A: Reverse level order
def level_order_reverse(root):
    """Variant A: return levels in reverse order"""
    return level_order_traversal(root)[::-1]

# VARIANT 2B: Zigzag traversal
def zigzag_level_order(root):
    """Variant B: zigzag traversal (left-to-right, then right-to-left)"""
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return result

# VARIANT 2C: Rightmost node per level
def rightmost_per_level(root):
    """Variant C: return rightmost node value per level"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        rightmost = None
        for _ in range(len(queue)):
            node = queue.popleft()
            rightmost = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(rightmost)
    return result

print("=== PROBLEM 2: LEVEL ORDER ===")
print("Level order:", level_order_traversal(tree))
print("Zigzag:", zigzag_level_order(tree))
print()


# ============================================================
# PROBLEM 3: VALIDATE BST
# ============================================================
# What it solves: Check if binary tree is valid BST
# Key: Track valid range for each node
# Interview angle: Find violating node? Min changes to fix?

# BASE: Validate BST
def is_valid_bst(root):
    """Base: check if binary tree is valid BST"""
    def helper(node, lower, upper):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
    return helper(root, float('-inf'), float('inf'))

# VARIANT 3A: Find first violating node
def find_violating_node(root):
    """Variant A: find first node that violates BST property"""
    def helper(node, lower, upper):
        if not node:
            return None
        if node.val <= lower or node.val >= upper:
            return node
        left_violation = helper(node.left, lower, node.val)
        if left_violation:
            return left_violation
        return helper(node.right, node.val, upper)
    return helper(root, float('-inf'), float('inf'))

# VARIANT 3B: Minimum changes to make valid BST
def min_changes_to_valid_bst(root):
    """Variant B: minimum node value changes to make valid BST"""
    def helper(node, lower, upper):
        if not node:
            return 0
        changes = 0
        if node.val <= lower or node.val >= upper:
            changes = 1
            node.val = (lower + upper) // 2
        changes += helper(node.left, lower, node.val)
        changes += helper(node.right, node.val, upper)
        return changes
    return helper(root, float('-inf'), float('inf'))

# VARIANT 3C: Count swaps needed
def count_swaps_fix_bst(root):
    """Variant C: count swaps needed to fix (inorder and sort then match)"""
    inorder_vals = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        inorder_vals.append(node.val)
        inorder(node.right)
    inorder(root)
    sorted_vals = sorted(inorder_vals)
    swaps = 0
    for i in range(len(inorder_vals)):
        if inorder_vals[i] != sorted_vals[i]:
            swaps += 1
    return swaps // 2

print("=== PROBLEM 3: VALIDATE BST ===")
bst = TreeNode(2)
bst.left = TreeNode(1)
bst.right = TreeNode(3)
print("Is valid BST:", is_valid_bst(bst))
print()


# ============================================================
# PROBLEM 4: NUMBER OF ISLANDS
# ============================================================
# What it solves: Count disconnected regions of 1s in 2D grid
# Strategy: DFS/BFS to mark visited cells, count regions
# Interview angle: Largest island? Perimeter?

# BASE: Count islands
def num_islands(grid):
    """Base: count number of islands (1s connected horizontally/vertically)"""
    if not grid:
        return 0
    islands = 0
    visited = set()

    def dfs(r, c):
        if (r, c) in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    return islands

# VARIANT 4A: Find largest island size
def largest_island(grid):
    """Variant A: area of largest island"""
    visited = set()

    def dfs(r, c):
        if (r, c) in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return 0
        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    max_size = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                max_size = max(max_size, dfs(r, c))
    return max_size

# VARIANT 4B: Return all island coordinates
def get_all_islands_coords(grid):
    """Variant B: return coordinates of all islands as separate lists"""
    visited = set()
    islands = []

    def dfs(r, c, island):
        if (r, c) in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        visited.add((r, c))
        island.append((r, c))
        dfs(r + 1, c, island)
        dfs(r - 1, c, island)
        dfs(r, c + 1, island)
        dfs(r, c - 1, island)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                island = []
                dfs(r, c, island)
                islands.append(island)
    return islands

# VARIANT 4C: Count with diagonal connectivity
def num_islands_diagonal(grid):
    """Variant C: count islands with 8-directional connectivity (diagonals)"""
    visited = set()

    def dfs(r, c):
        if (r, c) in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        visited.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    dfs(r + dr, c + dc)

    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    return islands

print("=== PROBLEM 4: NUMBER OF ISLANDS ===")
grid = [['1', '1', '0'], ['0', '1', '0'], ['1', '0', '1']]
print("Num islands:", num_islands(grid))
print("Largest island:", largest_island(grid))
print()

print("=" * 70)
print("CATEGORY 7: TREE/GRAPH PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Tree recursion (depth-first)")
print("Pattern 2: BFS level-order traversal")
print("Pattern 3: DFS/BFS graph connectivity")
print("=" * 70)
