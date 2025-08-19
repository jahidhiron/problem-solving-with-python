"""
binary_tree.py

This module provides functionality to generate a binary tree from a Python list
(using level-order representation) and print it in a readable, hierarchical format.

Example:
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    root = tree.generate_binary_tree(arr)
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
    """A utility class for creating and printing binary trees."""

    def generate_binary_tree_by_recursion(self, arr, i=0):
        """
        Recursively generate a binary tree from a list using level-order representation.
        
        Args:
            arr (list): List containing tree elements. 
                        `None` represents a missing node.
            i (int): Current index in the list.
        
        Returns:
            TreeNode: Root node of the generated binary tree.
        """
        if i >= len(arr) or arr[i] is None:
            return None 
        
        root = TreeNode(arr[i])
        root.left = self.generate_binary_tree_by_recursion(arr, i * 2 + 1)
        root.right = self.generate_binary_tree_by_recursion(arr, i * 2 + 2)
        
        return root

    def generate_binary_tree_by_queue(self, arr):
        """
        Recursively generate a binary tree from a list using level-order representation.
        
        Args:
            arr (list): List containing tree elements. 
                        `None` represents a missing node.
            i (int): Current index in the list.
        
        Returns:
            TreeNode: Root node of the generated binary tree.
        """
        if not arr:
            return None 
        
        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1
        
        while i < len(arr):
            current = queue.popleft()
            
            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)

            i+= 1

            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)

            i+= 1

        return root

    def print_tree(self, root, level=0, prefix="Root: "):
        """
        Print the binary tree structure in a hierarchical format.
        
        Args:
            root (TreeNode): The root of the binary tree.
            level (int): Current depth level in the tree (used for indentation).
            prefix (str): Prefix label to indicate branch type ("Root:", "L---", "R---").
        """
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    root1 = tree.generate_binary_tree_by_recursion(arr)
    root2 = tree.generate_binary_tree_by_queue(arr)

    print("Binary Tree Structure:")
    tree.print_tree(root1)
    tree.print_tree(root2)
