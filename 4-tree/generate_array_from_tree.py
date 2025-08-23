"""
binary_tree.py

This module provides functionality to generate a binary tree from a Python list
(using level-order representation), convert a tree back to a list (level-order
or pre-order), and print the tree in a readable, hierarchical format.

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
    """A utility class for creating, converting, and printing binary trees."""

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

        for i in range(len(nodes)):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[i].right = nodes[right_index]

        return nodes[0]

    def generate_array_from_tree(self, root):
        """
        Convert a binary tree to a list using level-order traversal.

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            list: List of node values in level-order.
        """
        if not root:
            return []

        queue = [root]
        arr = []

        for node in queue:
            arr.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return arr

    def generate_array_from_tree_by_recursive(self, root):
        """
        Convert a binary tree to a list using pre-order traversal (recursive).

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            list: List of node values in pre-order.
        """
        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.value)  # visit root
            dfs(node.left)             # visit left subtree
            dfs(node.right)            # visit right subtree

        dfs(root)
        return result

    def print_tree(self, root, level=0, prefix="Root: "):
        """
        Print the binary tree structure in a readable hierarchical format.

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

    arr_output = tree.generate_array_from_tree(root1)
    print("Level-order array:", arr_output)

    arr_output1 = tree.generate_array_from_tree_by_recursive(root1)
    print("Pre-order array:", arr_output1)
