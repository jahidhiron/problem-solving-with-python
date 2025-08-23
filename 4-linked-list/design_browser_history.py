"""
browser_history.py

A simple implementation of a Browser History using a doubly linked list.

This module defines:
- Node: A class representing a page in history with pointers to previous and next pages.
- BrowserHistory: A class to simulate visiting, moving backward, and moving forward in 
  a browser's history.

Example:
    >>> history = BrowserHistory("leetcode.com")
    >>> history.visit("google.com")
    >>> history.visit("facebook.com")
    >>> history.visit("youtube.com")
    >>> print(history.back(1))     # facebook.com
    >>> print(history.back(1))     # google.com
    >>> print(history.forward(1))  # facebook.com
    >>> history.visit("linkedin.com")
    >>> print(history.forward(2))  # linkedin.com
    >>> print(history.back(2))     # google.com
    >>> print(history.back(7))     # leetcode.com
"""


class Node:
    """
    Represents a single page in the browser history.

    Attributes:
        value (str): The URL of the page.
        prev (Node): Pointer to the previous page in history.
        next (Node): Pointer to the next page in history.
    """

    def __init__(self, value, p=None, n=None):
        """
        Initialize a Node instance.

        Args:
            value (str): The URL of the page.
            prev (Node, optional): The previous page node. Defaults to None.
            next (Node, optional): The next page node. Defaults to None.
        """
        self.value = value
        self.prev = p
        self.next = n


class BrowserHistory:
    """
    A browser history manager using a doubly linked list.

    Methods:
        visit(url): Visit a new URL and clear forward history.
        back(steps): Move back in history up to 'steps' times.
        forward(steps): Move forward in history up to 'steps' times.
    """

    def __init__(self, homepage):
        """
        Initialize the browser history with a homepage.

        Args:
            homepage (str): The starting homepage URL.
        """
        self.curr = Node(homepage)

    def visit(self, url):
        """
        Visit a new URL. Clears all forward history from the current page.

        Args:
            url (str): The new URL to visit.
        """
        self.curr.next = Node(url, p=self.curr)
        self.curr = self.curr.next

    def back(self, steps):
        """
        Move backward in history.

        Args:
            steps (int): The number of steps to move back.

        Returns:
            str: The current page's URL after moving back.
        """
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.value

    def forward(self, steps):
        """
        Move forward in history.

        Args:
            steps (int): The number of steps to move forward.

        Returns:
            str: The current page's URL after moving forward.
        """
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.value


if __name__ == "__main__":
    # Example usage
    history = BrowserHistory("leetcode.com")
    history.visit("google.com")
    history.visit("facebook.com")
    history.visit("youtube.com")
    print(history.back(1))     # facebook.com
    print(history.back(1))     # google.com
    print(history.forward(1))  # facebook.com
    history.visit("linkedin.com")
    print(history.forward(2))  # linkedin.com
    print(history.back(2))     # google.com
    print(history.back(7))     # leetcode.com
