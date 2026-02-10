#Stack
class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def length(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Number of items in the Stack are : ", self.size)
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            print("The Top most element is : ", self.items[self.size-1])
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("The Poped element is : ", self.items.pop())
            self.size -= 1

s = Stack()

print("Performed by 42 & 47")
print("Kindly select any option from the given menu :")
print("1.PUSH\n2.POP\n3.PEEK\n4.LENGTH\n5.EXIT")

ch = int(input("Enter your Choice : "))
while ch <= 4:
    if ch == 1:
        value = int(input("Enter the value to be inserted into the stack : "))
        s.push(value)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        print("The length of the stack is : ",s.length())
    elif ch == 5:
        break
    ch = int(input("Enter your choice : "))

#Queue

class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = queue()
print("Before inserting an element the length of Queue is : ", q.size())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("\nAfter inserting an element in the Queue : ")
q.display()

print("\nAfter inserting an element the length of Queue is : ",q.size())

q.dequeue()
print("\nAfter removing an element in the queue : ")
q.display()
print("\nAfter removing an element the length of Queue is : ", q.size())
