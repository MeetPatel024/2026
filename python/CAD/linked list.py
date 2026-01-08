class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singlylinkedlist:
    def __init__(self):
        self.head = None
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def travarsal(self):
        if self.head is None:
            print("empty")
        else: 
            curr = self.head
            while curr is not None:
                print(curr.val,end="->")
                curr = curr.next
            print('None')
            
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count<position:
                prev_node = curr
                curr  = curr.next
                count +=1
            prev_node.next = new_node
            new_node.next = curr
    
    def delete_at(self,position):
        if position==0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and count<position:
                prev = curr
                curr = curr.next
                count+=1
            prev.next = curr.next

    def delete_val(self,val):
        curr = self.head
        prev = None
        count = 0
        while curr is not None and curr.val!=val:
            prev = curr
            curr = curr.next
            count+=1
        if curr is None:
            print(val," not found")
            return 0
        prev.next = curr.next

sll = Singlylinkedlist()
sll.append(10)
sll.append(20)
sll.append(27)
sll.append(30)
sll.append(40)
sll.append(69)
sll.append(50)
print("list = ",end='')
sll.travarsal()

print("list after inset 35 at 3 = ",end='')
sll.insert_at(35,3)
sll.travarsal()

print("list after deleting 5th index = ",end='')
sll.delete_at(5)
sll.travarsal()

print("list after deleting 27 = ",end='')
sll.delete_val(27)
sll.travarsal()

print("if trying to delete val that is not presnt in list :")
sll.delete_val(102)