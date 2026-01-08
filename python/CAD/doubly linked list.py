class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
    
    #insert at begining
    def inset_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
    
    def travarsal(self):
        if not self.head:
            print("empty")
        else:
            curr = self.head
            while curr:
                print(curr.val,end="->")
                curr=curr.next
            print("none")

    def insert_at(self,val,position):
        new_node = Node(val)
        if not self.head:
            print("empty")
        else:
            count=0
            curr = self.head
            for _ in range(position):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next.prev = new_node

    def reverse_travarsal(self):
        if not self.head:
            print("empty")
        else:
            curr = self.head
            while curr:
                curr = curr.next
            while curr:
                print(curr.val,end="->")
                curr = curr.prev


        

dll = doubly_linked_list()
dll.inset_at_head(10)
dll.inset_at_head(41)
dll.inset_at_head(45)
dll.append(12)
dll.append(13)
dll.append(14)
dll.insert_at(69,2)
dll.travarsal()
dll.reverse_travarsal()