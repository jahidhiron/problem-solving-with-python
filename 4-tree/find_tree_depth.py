"""
binary_tree.py

This module provides functionality to generate a binary tree from a Python list
(using level-order representation), calculate its maximum depth, and print it
in a readable hierarchical format.

Example:
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    root = tree.generate_binary_tree_by_array(arr)
    tree.print_tree(root)

Output:
    Root: 1
        L--- 2
            L--- 4
            R--- 5
        R--- 3
            L--- 6
            R--- 7
"""

from collections import deque


class TreeNode:
    """Represents a single node in a binary tree."""

    def __init__(self, value):
        """
        Initialize a tree node.

        Args:
            value (any): The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class Tree:
    """A utility class for creating, printing, and analyzing binary trees."""

    def generate_binary_tree_by_array(self, arr):
        """
        Generate a binary tree from a list using level-order traversal.

        Each element in the input list represents a node in level-order. A value of
        `None` indicates that the corresponding node is missing.

        Args:
            arr (list): List containing tree elements in level-order.

        Returns:
            TreeNode: Root node of the generated binary tree, or None if the list is empty.

        Example:
            >>> arr = [1, 2, 3, None, 4]
            >>> tree = Tree()
            >>> root = tree.generate_binary_tree_by_array(arr)
        """
        if not arr:
            return None

        nodes = []

        for val in arr:
            nodes.append(None if val is None else TreeNode(val))

        for i, _node in enumerate(nodes):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[i].right = nodes[right_index]

        return nodes[0]

    def tree_max_depth(self, root):
        """
        Compute the maximum depth of the binary tree.

        Depth is defined as the number of nodes along the longest path from the root
        node down to the farthest leaf node.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: Maximum depth of the tree.

        Example:
            >>> tree = Tree()
            >>> root = tree.generate_binary_tree_by_array([1, 2, 3])
            >>> tree.tree_max_depth(root)
            2
        """
        depth = 0

        def dfs(node, level):
            nonlocal depth
            if node is None:
                return
            depth = max(depth, level)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return depth

    def print_tree(self, root, level=0, prefix="Root: "):
        """
        Print the binary tree in a readable, hierarchical format.

        Args:
            root (TreeNode): The root node of the binary tree.
            level (int, optional): Current depth level (used for indentation). Defaults to 0.
            prefix (str, optional): Label prefix for the current node. Defaults to "Root: ".

        Example:
            >>> tree = Tree()
            >>> root = tree.generate_binary_tree_by_array([1, 2, 3])
            >>> tree.print_tree(root)
            Root: 1
                L--- 2
                R--- 3
        """
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")


if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    root1 = tree.generate_binary_tree_by_array(input_array)
    print("Binary Tree Structure:")
    tree.print_tree(root1)

    tree_depth = tree.tree_max_depth(root1)
    print("Tree Depth:", tree_depth)
