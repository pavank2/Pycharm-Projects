#Implement linked List

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

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def reverse_list(self):
        prev = None
        curr = self.head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def swapInPairs(self):

        dummy = Node(0)
        dummy.next = self.head
        current = dummy

        while current.next and current.next.next:
            # Nodes to be swapped
            node1 = current.next
            node2 = current.next.next

            # Swapping
            current.next = node2
            node1.next = node2.next
            node2.next = node1

            # Move to the next pair
            current = node1

       # return dummy.next






llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(32)
llist.insert(30)
llist.insert(62)
llist.insert(40)
#llist.reverse_list()
#llist.display()
llist.swapInPairs()
llist.display()
