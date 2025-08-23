"""
doubly_linked_list.py

This module implements a doubly linked list with operations for insertion, deletion, and access
at specific indices, using head and tail sentinel nodes.
"""


class Node:
    """
    A node in a doubly linked list.
    """

    def __init__(self, val, n=None, p=None):
        self.val = val
        self.next = n
        self.prev = p


class MyLinkedList:
    """
    A doubly linked list implementation with sentinel head and tail nodes.
    """

    def __init__(self):
        """
        Initialize an empty linked list with sentinel nodes.
        """
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _get_nth_node(self, curr, index):
        """
        Get the node at the specified index starting from curr.

        Args:
            curr (Node): Starting node.
            index (int): Index to reach.

        Returns:
            Node: Node at index.
        """
        while curr and index > 0:
            curr = curr.next
            index -= 1
        return curr

    def get(self, index):
        """
        Get the value at the specified index.

        Args:
            index (int): Index to retrieve.

        Returns:
            int: Value at index, or -1 if invalid.
        """
        if index < 0 or index >= self.size:
            return -1
        node = self._get_nth_node(self.head.next, index)
        return node.val

    def _insert(self, val, prev_node, next_node):
        """
        Insert value between two nodes.

        Args:
            val (int): Value to insert.
            prev_node (Node): Previous node.
            next_node (Node): Next node.
        """
        new_node = Node(val)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    def add_at_head(self, val):
        """
        Insert value at the head of the list.

        Args:
            val (int): Value to insert.
        """
        self._insert(val, self.head, self.head.next)

    def add_at_tail(self, val):
        """
        Insert value at the tail of the list.

        Args:
            val (int): Value to insert.
        """
        self._insert(val, self.tail.prev, self.tail)

    def add_at_index(self, index, val):
        """
        Insert value before index.

        Args:
            index (int): Position to insert at.
            val (int): Value to insert.
        """
        if index < 0 or index > self.size:
            return
        prev_node = self._get_nth_node(self.head, index)
        self._insert(val, prev_node, prev_node.next)

    def _delete_node(self, node):
        """
        Delete a node from the list.

        Args:
            node (Node): Node to delete.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def delete_at_index(self, index):
        """
        Delete node at the given index.

        Args:
            index (int): Index to delete.
        """
        if index < 0 or index >= self.size:
            return
        node = self._get_nth_node(self.head.next, index)
        self._delete_node(node)


def print_list(linked_list):
    """
    Print all nodes in a singly linked list in a readable format.

    Args:
        linked_list (Node): The head node of the linked list.

    Example:
        For a linked list 10 -> 10 -> 20 -> 30 -> 40 -> None, the output will be:
        1 -> 2 -> 3 -> None
    """
    while linked_list:
        print(linked_list.val, end=" -> ")
        linked_list = linked_list.next
    print("None")


# Example usage:
if __name__ == "__main__":
    ll = MyLinkedList()
    ll.add_at_head(10)
    ll.add_at_tail(20)
    ll.add_at_index(1, 15)  # List: 10 -> 15 -> 20
    print_list(ll.head)
    print(ll.get(0))  # Output: 10
    print(ll.get(1))  # Output: 15

    ll.delete_at_index(1)  # Delete 15
    print(ll.get(1))  # Output: 20
    print_list(ll.head)
