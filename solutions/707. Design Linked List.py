# Solution 1: Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if (index < 0) or (index >= self.size):
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if (index < 0) or (index > self.size):
            return
        
        node = Node(val)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        
        self.size += 1
        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if (index < 0) or (index >= self.size):
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1


# TODO:
# Doubly linked list
