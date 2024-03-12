#Given the head of a singly linked list, group all the nodes with odd indices together
# followed by the nodes with even indices, and return the reordered list.

#'The first node is considered odd, and the second node is even, and so on.

# NOT WORKING
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self,item):
         new_node = Node(item)

         if self.head == None:
             self.head = new_node
             return

         curr_node = self.head

         while curr_node.next:
             curr_node = curr_node.next

         curr_node.next = new_node

    def displayNodes(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.item)
            curr_node = curr_node.next

    def listOddEven(self):
         temp_odd_index_list = []

         prev_node = self.head
         curr_node = self.head.next


         while prev_node.next:
               print(prev_node.item)
               #temp_odd_index_list.append(prev_node.next.item)
               curr_node = prev_node
               prev_node = prev_node.next.next
               curr_node.next = None


         for num in temp_odd_index_list:
             new_node = Node(num)
             curr_node.next = new_node



llist = LinkedList()
llist.insertNode(10)
llist.insertNode(20)
llist.insertNode(30)
llist.insertNode(40)
llist.insertNode(50)
llist.insertNode(60)
llist.insertNode(70)

llist.listOddEven()
#llist.displayNodes()
