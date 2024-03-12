
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

    def make_circular(self):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = self.head
        return

    def detectCircular(self):
        curr = self.head


        while curr.next is not None and curr.next is not self.head:
            curr = curr.next

        if curr.next == self.head:
            return("Circular")
        else:
            return("Not circular")

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(32)
llist.insert(30)
llist.make_circular()
print(llist.detectCircular())