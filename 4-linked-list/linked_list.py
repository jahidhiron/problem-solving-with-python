"""
Linked List Module

This module implements a basic singly linked list in Python, including
operations for appending, prepending, inserting after a given node,
deleting nodes, searching for values, and displaying the list.

Classes:
    Node: Represents a single node in the linked list.
    LinkedList: Implements the linked list and its operations.

Example:
    >>> ll = LinkedList()
    >>> ll.append(10)
    >>> ll.append(20)
    >>> ll.append(30)
    >>> ll.display()
    10 -> 20 -> 30 -> None
"""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (any): The value stored in the node.
        next (Node): A reference to the next node in the list.
    """

    def __init__(self, data):
        """
        Initialize a new node.

        Args:
            data (any): The value to store in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Append a new node with the given data at the end of the list.

        Args:
            data (any): The value to store in the new node.
        """
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        """
        Insert a new node with the given data at the beginning of the list.

        Args:
            data (any): The value to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """
        Insert a new node with the given data after the specified node.

        Args:
            prev_node (Node or any): The node (or its value) after which the new node should be inserted.
            data (any): The value to store in the new node.

        Notes:
            - If `prev_node` is a Node object, it is matched by reference.
            - If `prev_node` is a value, it is matched by comparing data values.
        """
        current = self.head
        while current:
            if current == prev_node or current.data == prev_node:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node} not found.")

    def delete_node(self, key):
        """
        Delete the first node in the list that contains the given value.

        Args:
            key (any): The value of the node to delete.
        """
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        prev.next = current.next
        current = None

    def search(self, key):
        """
        Search for a node containing the given value.

        Args:
            key (any): The value to search for.

        Returns:
            bool: True if a node with the given value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """
        Print the linked list in a readable format.

        Example:
            10 -> 20 -> 30 -> None
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def merge_two_sorted_lists(self, list1, list2):
        """
        Merge two sorted linked lists into one sorted linked list.

        Args:
            other (LinkedList): Another linked list to merge with.

        Returns:
            LinkedList: A new linked list containing the merged values.
        """
        dummy_head = Node(-1)
        current = dummy_head

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy_head.next

    def middle_of_the_linked_list(self, linked_list):
        """
        Find the middle node of a singly linked list using the slow and fast pointer technique.

        The slow pointer moves one step at a time, while the fast pointer moves two steps.
        When the fast pointer reaches the end of the list, the slow pointer will be at the middle.

        Args:
            linked_list (ListNode): The head node of the singly linked list.

        Returns:
            ListNode: The middle node of the linked list. 
                    If the list has an even number of nodes, returns the second middle node.
        """
        if not linked_list.next:
            return None

        slow = linked_list
        fast = linked_list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def before_middle_of_the_linked_list(self, linked_list):
        """
        Find the node before the middle node of a singly linked list.

        Args:
            linked_list (ListNode): The head node of the singly linked list.

        Returns:
            ListNode: The node before the middle node of the linked list.
        """
        if not linked_list or not linked_list.next:
            return None

        slow = linked_list
        fast = linked_list.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def delete_middle_node(self, linked_list):
        """
        Delete the middle node of a singly linked list.

        Args:
            linked_list (ListNode): The head node of the singly linked list.

        Returns:
            ListNode: The head of the modified linked list after deleting the middle node.
        """
        head = linked_list
        if not head or not head.next:
            return None

        slow = self.middle_of_the_linked_list(linked_list)
        slow.next = slow.next.next

        return head

    def remove_nth_from_end(self, head, n):
        """
        Remove the nth node from the end of a singly linked list.

        Args:
            head (Node): The head node of the linked list.
            n (int): The position from the end (1-indexed) of the node to remove.

        Returns:
            Node: The head of the modified linked list.

        Raises:
            ValueError: If n is less than 1 or greater than the length of the list.

        Example:
            Given the linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2
            After removal: 10 -> 10 -> 20 -> 40 -> None
        """
        dummy = Node(-1)
        dummy.next = head
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

    def reverse_linked_list_iterative_approach(self, head):
        """
        Reverse a singly linked list.

        Args:
            head (Node): The head node of the linked list.

        Returns:
            Node: The new head of the reversed linked list.
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def reverse_linked_list_recursive_approach(self, head):
        """
        Reverse a singly linked list using recursion.

        Args:
            head (Node): The head node of the linked list.

        Returns:
            Node: The new head of the reversed linked list.
        """
        if not head:
            return None

        current = head

        if head.next:
            current = self.reverse_linked_list_recursive_approach(head.next)

            right = head.next
            right.next = head

        head.next = None

        return current

    def reoder_linked_list(self, head):
        """
        Reorder a singly linked list in-place.

        The reordering is done such that the nodes are arranged in the order:
        first node, last node, second node, second last node, and so on.

        Args:
            head (Node): The head node of the linked list.

        Returns:
            Node: The head of the reordered linked list.
        """
        if not head or not head.next or not head.next.next:
            return head

        before_mid = self.before_middle_of_the_linked_list(head)
        second_half = before_mid.next
        second_half_reverse = self.reverse_linked_list_iterative_approach(
            second_half)
        before_mid.next = None
        first_half = head
        second_half = second_half_reverse

        while second_half.next:
            first_half_next = first_half.next
            second_half_next = second_half.next

            first_half.next = second_half
            second_half.next = first_half_next

            first_half = first_half_next
            second_half = second_half_next

        return head

    def has_cycle(self, head):
        """
        Detects if a singly linked list has a cycle.

        This function uses Floyd's Tortoise and Hare algorithm to determine
        whether a cycle exists in the linked list. It uses two pointers,
        moving at different speeds, and if they ever meet, a cycle exists.

        Args:
            head (Node): The head node of the linked list.

        Returns:
            bool: True if the linked list contains a cycle, False otherwise.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False


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
        print(linked_list.data, end=" -> ")
        linked_list = linked_list.next
    print("None")


if __name__ == "__main__":
    # Example usage
    # ll = LinkedList()

    # ll.append(10)
    # ll.append(20)
    # ll.append(30)
    # # ll.display()   # 10 -> 20 -> 30 -> None

    # ll.prepend(5)
    # ll.display()   # 5 -> 10 -> 20 -> 30 -> None

    # ll.insert_after(ll.head.next, 15)  # insert after node with value 10
    # # ll.display()   # 5 -> 10 -> 15 -> 20 -> 30 -> None

    # ll.delete_node(20)
    # # ll.display()   # 5 -> 10 -> 15 -> 30 -> None

    # # print(ll.search(30))  # True
    # # print(ll.search(99))  # False

    l1 = LinkedList()
    l1.append(10)
    l1.append(20)
    l1.append(30)

    l2 = LinkedList()
    l2.append(10)
    l2.append(30)
    l2.append(40)

    merged_list = l1.merge_two_sorted_lists(l1.head, l2.head)
    print_list(merged_list)  # 10 -> 10 -> 20 -> 30 -> 30 -> 40 -> None

    middle_linked_list = l1.middle_of_the_linked_list(merged_list)
    print_list(middle_linked_list)  # 30 -> 30 -> 40 -> None

    rest_linked_list = l1.delete_middle_node(merged_list)
    print_list(rest_linked_list)  # 10 -> 10 -> 20 -> 30 -> 40 -> None

    remove_nth_list_form_end = l1.remove_nth_from_end(rest_linked_list, 2)
    print_list(remove_nth_list_form_end)  # 10 -> 10 -> 20 -> 40 -> None

    reversed_list = l1.reverse_linked_list_iterative_approach(
        remove_nth_list_form_end)
    print_list(reversed_list)  # 40 -> 20 -> 10 -> 10 -> None

    reversed_list1 = l1.reverse_linked_list_recursive_approach(
        reversed_list)
    print_list(reversed_list1)  # 10 -> 10 -> 20 -> 40 -> None

    reoder_list = l1.reoder_linked_list(
        reversed_list1)
    print_list(reoder_list)  # 10 -> 40 -> 10 -> 20 -> None
