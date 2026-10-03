# ============================================================
# Category 7: Tree / Graph Problems
# Core pattern: BFS/DFS traversal, recursion, visited tracking
# ============================================================

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


# O(n) time, O(h) space (h = height, recursion stack)
def max_depth_tree(root):
    if not root:
        return 0
    return 1 + max(max_depth_tree(root.left), max_depth_tree(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("max_depth_tree:", max_depth_tree(root))


# O(n) time, O(n) space
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

print("level_order_traversal:", level_order_traversal(root))


# O(n) time, O(h) space
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if root.value <= lo or root.value >= hi:
        return False
    return is_valid_bst(root.left, lo, root.value) and is_valid_bst(root.right, root.value, hi)

bst = TreeNode(2)
bst.left = TreeNode(1)
bst.right = TreeNode(3)
print("is_valid_bst:", is_valid_bst(bst))


# O(n) time, O(n) space
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r, c) in visited:
            return
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    return islands

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print("num_islands:", num_islands(grid))


# O(n) time, O(n) space
def has_path_graph(graph, start, end):
    if start == end:
        return True
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        if node == end:
            return True
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        return False

    return dfs(start)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}
print("has_path_graph (a to d):", has_path_graph(graph, 'a', 'd'))


# O(n) time, O(h) space  [MIXED: tree + list-building]
def inorder_traversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.value)
        inorder(node.right)
    inorder(root)
    return result

print("inorder_traversal:", inorder_traversal(root))


# O(n) time, O(n) space
def path_sum(root, target):
    result = []
    def dfs(node, curr_sum, path):
        if not node:
            return
        path.append(node.value)
        curr_sum += node.value
        if not node.left and not node.right and curr_sum == target:
            result.append(path[:])
        dfs(node.left, curr_sum, path)
        dfs(node.right, curr_sum, path)
        path.pop()
    dfs(root, 0, [])
    return result

path_tree = TreeNode(5)
path_tree.left = TreeNode(4)
path_tree.right = TreeNode(8)
path_tree.left.left = TreeNode(11)
path_tree.left.left.left = TreeNode(7)
path_tree.left.left.right = TreeNode(2)
print("path_sum (target=22):", path_sum(path_tree, 22))


# O(n) time, O(n) space
def lowest_common_ancestor(root, p, q):
    if not root or root.value == p or root.value == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

lca_tree = TreeNode(3)
lca_tree.left = TreeNode(5)
lca_tree.right = TreeNode(1)
lca_tree.left.left = TreeNode(6)
lca_tree.left.right = TreeNode(2)
print("lowest_common_ancestor (5, 1):", lowest_common_ancestor(lca_tree, 5, 1).value)
