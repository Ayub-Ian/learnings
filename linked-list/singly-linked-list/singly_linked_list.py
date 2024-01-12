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
        self.size = 0

    # Traverse - access each element of the linked list
    def display_list(self):
        head = self.head
        while head is not None:
            print(head.data, end=("--->"))
            head = head.next

    # Insert at the beginning
    def insert_beginning(self, new_data):
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
    
    # Insert at the end
    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def delete_node(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False
    
    # Sort the linked list
    def sort_list(self):
        current = self.head
        index = Node(None)

        if self.head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def list_size(self):
        current = self.head

        if current is None:
            return None
        while current is not None:
            current = current.next
            self.size += 1
        return self.size

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

    linked_list.sort_list()

    # Print the linked list item
    linked_list.display_list()

    print(linked_list.list_size())
