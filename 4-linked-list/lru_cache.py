"""
lru_cache.py

This module implements a Least Recently Used (LRU) Cache using a HashMap and a Doubly Linked List.
The cache has a fixed capacity and supports O(1) operations for both get and put.

Author: Jahid Hiron
"""


class Node:
    """
    Represents a node in a doubly linked list for storing key-value pairs.
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly linked list to maintain the usage order of the cache.
    The most recently used node is placed before the tail.
    """

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """
        Removes a node from the list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_before_tail(self, node):
        """
        Adds a node just before the tail (most recently used).
        """
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Methods
    -------
    get(key): Returns the value for the given key if it exists, else -1.
    put(key, value): Inserts or updates the value for the given key.
    """

    def __init__(self, capacity):
        """
        Initializes the cache with a given capacity.
        """
        self.capacity = capacity
        self.map = {}
        self.list = DoublyLinkedList()

    def get_node(self, key):
        """
        Retrieves the node and updates its usage to most recently used.
        """
        if key not in self.map:
            return None
        node = self.map[key]
        self.list.remove(node)
        self.list.add_before_tail(node)
        return node

    def remove_after_head(self):
        """
        Removes and returns the least recently used node (after head).
        """
        first_node = self.list.head.next
        if first_node == self.list.tail:
            return None
        self.list.remove(first_node)
        return first_node

    def get(self, key):
        """
        Returns the value associated with the key, or -1 if not present.
        """
        node = self.get_node(key)
        return node.val if node else -1

    def evict_lru(self):
        """
        Evicts the least recently used node from the cache.
        """
        node_removed = self.remove_after_head()
        if node_removed and node_removed.key in self.map:
            del self.map[node_removed.key]

    def write_in_cache(self, key, value):
        """
        Inserts a new key-value node in the cache and handles eviction if needed.
        """
        new_node = Node(key, value)
        self.map[key] = new_node
        self.list.add_before_tail(new_node)

        if len(self.map) > self.capacity:
            self.evict_lru()

    def put(self, key, value):
        """
        Adds a key-value pair to the cache or updates an existing one.
        """
        node_exist = self.get_node(key)
        if node_exist:
            node_exist.val = value
        else:
            self.write_in_cache(key, value)


if __name__ == "__main__":
    # Initialize cache with capacity 2
    cache = LRUCache(2)

    cache.put(1, 100)     # Cache: {1=100}
    cache.put(2, 200)     # Cache: {1=100, 2=200}
    print(cache.get(1))   # Output: 100 (1 is now most recently used)

    cache.put(3, 300)     # Evicts key 2, Cache: {1=100, 3=300}
    print(cache.get(2))   # Output: -1 (not found)

    cache.put(4, 400)     # Evicts key 1, Cache: {3=300, 4=400}
    print(cache.get(1))   # Output: -1 (not found)
    print(cache.get(3))   # Output: 300
    print(cache.get(4))   # Output: 400
