# Python Linked List Example with Common Methods

# Linked lists are made of nodes where each node contains data and a pointer to the next node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append: Add a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print: Display the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Find: Search for a node with a specific value
    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    # Remove: Remove a node with a specific value
    def remove(self, key):
        current = self.head

        # If the head node is the one to be removed
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    # Insert After: Insert a new node after a specific node
    def insert_after(self, prev_node_data, new_data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node with data", prev_node_data, "not found.")

# Creating a linked list
ll = LinkedList()
ll.append("cats")
ll.append("dogs")
ll.append("birds")

print("Linked List Example:")
ll.print_list()

# Find node example
print("Finding 'dogs':", ll.find("dogs").data if ll.find("dogs") else "Not found")

# Remove node example
print("Removing 'dogs' from the linked list:")
ll.remove("dogs")
ll.print_list()

# Insert After example
print("Inserting 'fish' after 'cats':")
ll.insert_after("cats", "fish")
ll.print_list()

