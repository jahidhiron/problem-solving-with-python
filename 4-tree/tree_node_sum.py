"""
binary_tree.py

This module provides functionality to generate a binary tree from a Python list
(using level-order representation), calculate node and leaf sums, and print it
in a readable, hierarchical format.

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
        `None` indicates a missing node.

        Args:
            arr (list): List containing tree elements in level-order.

        Returns:
            TreeNode: Root node of the generated binary tree, or None if the list is empty.
        """
        if not arr:
            return None

        nodes = [None if val is None else TreeNode(val) for val in arr]

        for i, node in enumerate(nodes):
            if node is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    node.left = nodes[left_index]
                if right_index < len(nodes):
                    node.right = nodes[right_index]

        return nodes[0]

    def tree_node_summation(self, root):
        """
        Calculate the sum of all node values in the binary tree.

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            int or float: Sum of all node values.
        """
        node_sum = 0

        def dfs(node):
            nonlocal node_sum
            if node is None:
                return
            node_sum += node.value
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return node_sum

    def tree_leaf_node_summation(self, root):
        """
        Calculate the sum of all leaf node values in the binary tree.

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            int or float: Sum of all leaf node values.
        """
        leaf_sum = 0

        def dfs(node):
            nonlocal leaf_sum
            if node is None:
                return
            if node.left is None and node.right is None:
                leaf_sum += node.value
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return leaf_sum

    def print_tree(self, root, level=0, prefix="Root: "):
        """
        Print the binary tree in a readable, hierarchical format.

        Args:
            root (TreeNode): Root node of the binary tree.
            level (int): Current depth level for indentation.
            prefix (str): Label for the current node ("Root:", "L---", "R---").
        """
        if root:
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

    tree_node_sum = tree.tree_node_summation(root1)
    tree_leaf_node_sum = tree.tree_leaf_node_summation(root1)

    print("\nSum of all nodes:", tree_node_sum)
    print("Sum of leaf nodes:", tree_leaf_node_sum)
