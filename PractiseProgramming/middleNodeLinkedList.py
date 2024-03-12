# Find the middle node of the Linked List

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next




    def middleNode(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(32)
llist.insert(30)
llist.insert(3)
llist.insert(23)

print(llist.middleNode())
