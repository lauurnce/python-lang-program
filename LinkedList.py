class Node:
    """
    Represents an individual node in the linked list.
    A node holds the data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially points to nothing

class LinkedList:
    """
    Manages the linked list operations.
    It keeps track of the 'head' (first node) of the list.
    """
    def __init__(self):
        self.head = None  # The list starts empty

    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None

    def insert_at_beginning(self, data):
        """Inserts a new node at the start of the list (new head)."""
        new_node = Node(data)
        new_node.next = self.head  # New node's next points to the old head
        self.head = new_node        # Update the head to the new node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            print(f"Inserted {data} as the head.")
            return

        # Traverse the list to find the last node
        last = self.head
        while last.next:
            last = last.next

        # Change the next pointer of the last node
        last.next = new_node
        print(f"Inserted {data} at the end.")

    def display(self):
        """Prints the content of the list from head to tail."""
        if self.is_empty():
            print("Linked List: [] (Empty)")
            return

        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next

        # Join the nodes with ' -> ' to visualize the link
        print(f"Linked List: {' -> '.join(nodes)}")

    def search(self, key):
        """Searches for a specific value (key) in the list."""
        current = self.head
        position = 0

        while current:
            if current.data == key:
                print(f"Found {key} at position {position}.")
                return True
            current = current.next
            position += 1

        print(f"{key} not found in the list.")
        return False

# --- Demonstration ---
print("--- Linked List Demonstration ---")
my_list = LinkedList()
my_list.display()

# 1. Insert at the end
print("\n--- Insert at End ---")
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.display()

# 2. Insert at the beginning
print("\n--- Insert at Beginning ---")
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(0)
my_list.display()

# 3. Search operation
print("\n--- Search Operation ---")
my_list.search(20)
my_list.search(100)