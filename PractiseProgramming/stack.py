class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0


    def push_item(self,item):
        self.stack.append(item)

    def pop_item(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            raise IndexError("No items in stack")

    def peek(self):
        if not self.is_empty():
            print (self.stack[-1])
        else:
            raise IndexError("No items in stack")

    def display_items(self):
        if not self.is_empty():
            print (self.stack)
        else:
            raise IndexError("No items in stack")


stack = Stack()
stack.push_item(10)
stack.push_item(20)
stack.push_item(30)
stack.display_items()

stack.peek()
stack.pop_item()
stack.display_items()
