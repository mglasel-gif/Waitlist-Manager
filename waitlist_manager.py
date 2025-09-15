# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None

# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self,name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} was added to the front of the waitlist.")

    def add_end(self,name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            print(f"{name} was added to the end of the waitlist.")
            return

        last_node = self.head  
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"{name} was added to the end of the waitlist.")

    def remove(self,name):
        if self.head is None:
            print(f"'{name}' was not found in the waitlist.")
            return
        
        if self.head.name == name:
            self.head = self.head.next
            print(f"{name} was removed from the waitlist.")
            return
        
        while current_node:
            if current_node.name == name:
                previous_node.next = current_node.next
                print(f"{name} was removed from the waitlist.")
                return
            previous_node = current_node
            current_node = current_node.next

        print(f"'{name}' was not found in the waitlist.")

    def print_list(self):
        if not self.head:
            print("The waitlist is empty.")
            return

        current_node = self.head
        while current_node:
            print(f" - {current_node.name}")
            current_node = current_node.next

def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()          

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
The list is used to create a waitlist for customers using a linked list. It contains a Node to represent each customer. The list has an option to add a customer to the front or end of the list, remove customers and print the waitlist.

- What role does the head play?
The head is the first node and it is used as the starting point of the list. It also helps to check if the list is empty and add new nodes to the front of the list.

- When might a real engineer need a custom list like this?
A real engineer might use a custom list when doing a software application that requires a waitlist system, to add and remove customers in a specific order.
'''
