# Single Linked List Implementation and its operations
# Author: Ian Ayub

class Node:
    def __init__(self, value = None) -> None:
        self.data = value
        self.next = None

class LinkedList:
    '''
    Represents the linked list itself. It has an attribute head which initially points to None, 
    indicating an empty list.
    '''
    def __init__(self) -> None:
        self.head = None

    # Traverse - access each element of the linked list
    def display_list(self):
        head = self.head
        while head is not None:
            print(head.data, end=("--->"))
            head = head.next

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insert_after(self, prev_node, new_data):

        if prev_node is None:
            print("Element does not exist in the list.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

if __name__ == "__main__":
    linked_list = LinkedList()

    # Assign data values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    linked_list.insert_after(second, 4)

    # Print the linked list item
    linked_list.display_list()