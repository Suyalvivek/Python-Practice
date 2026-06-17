class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node



    def print_ll(self):
        temp = self.head
        while temp:
            print(f'{temp.data} --> ',end='')
            temp = temp.next

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        return count

    def insert_at_index(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('index out of range')
        if index==0:
            self.insert_at_beginning(data)
        count=0
        temp=self.head
        while temp:
            if count==index-1:
               new_node = Node(data)
               new_node.next = temp.next
               temp.next = new_node
               break
            count+=1
            temp=temp.next

    def remove_at_index(self,index):
        temp = self.head
        if index<0 or index>self.length():
            raise Exception('index out of range')
        if index==0:
            self.head = self.head.next
            return
        count = 0
        while temp:
            if count == index-1 :
                temp.next = temp.next.next
                break
                break;
            temp= temp.next
            count += 1

ll = LinkedList()
ll.insert_at_beginning('c')
ll.insert_at_beginning('b')
ll.insert_at_beginning('a')
ll.insert_at_end('d')
ll.print_ll()
ll.insert_at_index(2,'vivi')
ll.print_ll()
print('\n')
