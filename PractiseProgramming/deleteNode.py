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

    def deleteNode(self,deletedData):
        if self.head.data == deletedData:
            self.head = self.head.next
            return

        curr = self.head.next
        prev = self.head
        found = 0
        while curr:
            if curr.data == deletedData:
                prev.next = curr.next
                curr.next = None
                found = 1
                return
            else:
                prev = curr
                curr = curr.next

        if curr == None:
            print("Not found")
            return


    def displayList(self):
        curr = self.head

        while curr.next is not None:
            print(curr.data)
            curr = curr.next

llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(32)
llist.insert(30)
llist.insert(20)
llist.insert(23)

llist.deleteNode(4)
print(llist.displayList())
