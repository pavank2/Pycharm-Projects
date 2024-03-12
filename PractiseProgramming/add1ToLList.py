# A number N is represented in Linked List such that each digit corresponds to a node in linked list.
# You need to add 1 to it.

#Input:
#LinkedList: 4->5->6
#Output: 457

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

    def count_sum(self):
        data_list = []

        current_node = self.head
        while current_node is not None:
            data_list.append(current_node.data)
            current_node = current_node.next

        print(data_list)
        l = len(data_list)
        i = l - 1
        sum_list = 0
        while i >= 0:
            sum_list = sum_list + data_list[i]*pow(10,l-i-1)
            i = i - 1

        return sum_list + 1

    def display(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()
llist.insert(3)
llist.insert(4)
llist.insert(8)
print(llist.count_sum())