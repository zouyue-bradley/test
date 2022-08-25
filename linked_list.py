# A simple Python program to introduce a linked list
  
# Node class
class Node:
  
    # Function to initialise the node object
    def __init__(self, val):
        self.val = val  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
  
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    print(llist)
    print(llist.head.next)