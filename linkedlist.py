class Node:
    def __init__(self,data):
        self.data=data
        self.nextval=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printll(self):
        start=self.head
        while start is not None:
            print(start.data," ")
            start=start.nextval
            
    def insert_at_head(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        new_node=Node(data)
        new_node.nextval=self.head
        self.head=new_node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.nextval is not None:
            temp=temp.nextval
        temp.nextval=Node(data)
        
    def search(self,val):
        temp=self.head
        while temp is not None:
            if temp.data == val:
                return True
            temp=temp.nextval
        return False
        
    def length(self):
        temp=self.head
        cnt=0
        while temp is not None:
            cnt+=1
            temp=temp.nextval
        return cnt
    
    def reverse(self):
        cur=self.head
        prev=None
        ahead=None
        while cur is not None:
            ahead=cur.nextval
            cur.nextval=prev
            prev=cur
            cur=ahead
        self.head=prev
            
ll=LinkedList()
ll.insert_at_end("Sat")
#ll.head=Node("Mon")
#ll.head.nextval=Node("Tue")
#ll.head.nextval.nextval=Node("Wed")
#ll.insert_at_head("Sun")
#ll.insert_at_end("Thurs")
ll.printll()

