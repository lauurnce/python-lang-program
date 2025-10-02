## Python Implementation of a Stack using a List

class Stack:
    """
    A simple implementation of the Stack data structure using Python's list.
    LIFO (Last-In, First-Out) principle is enforced.
    """
    def __init__(self):
        # Initialize an empty list to hold the stack elements
        self.items = []

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return not self.items

    def push(self, item):
        """Adds a new item to the top of the stack (the end of the list)."""
        # The 'append()' method acts as the push operation
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Removes and returns the item from the top of the stack (the end of the list)."""
        if self.is_empty():
            # Prevent popping from an empty stack
            return "Error: Cannot pop from an empty stack."
        else:
            # The 'pop()' method removes and returns the last element (LIFO)
            return self.items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            return "Error: Stack is empty."
        else:
            # The last element is at index -1
            return self.items[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def display(self):
        """Prints the current contents of the stack."""
        if self.is_empty():
            print("Stack: [] (Empty)")
        else:
            # We display from top-to-bottom for better visualization
            print(f"Stack (Top -> Bottom): {self.items[::-1]}")


# --- Demonstration ---
print("--- Stack Demonstration ---")
my_stack = Stack()
my_stack.display() # Should show an empty stack

# 1. Pushing elements
print("\n--- Pushing Elements ---")
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display() # 30 should be at the top

# 2. Peeking at the top element
print("\n--- Peeking ---")
top_item = my_stack.peek()
print(f"Item at the top (Peek): {top_item}")
print(f"Current size: {my_stack.size()}")

# 3. Popping elements (LIFO: 30 should come out first)
print("\n--- Popping Elements ---")
popped_item_1 = my_stack.pop()
print(f"Popped: {popped_item_1}")
my_stack.display()

popped_item_2 = my_stack.pop()
print(f"Popped: {popped_item_2}")
my_stack.display()

# 4. Popping the last element
print("\n--- Final Pop ---")
popped_item_3 = my_stack.pop()
print(f"Popped: {popped_item_3}")
my_stack.display()

# 5. Attempting to pop from an empty stack
print("\n--- Popping from Empty Stack ---")
empty_pop_result = my_stack.pop()
print(empty_pop_result)