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
        
    def delete_at_head(self):
        temp=self.head.nextval
        self.head.nextval=None
        self.head=temp
        
    def delete_at_tail(self):
        cur=self.head
        prev=None
        while cur.nextval is not None:
            prev=cur
            cur=cur.nextval
        prev.nextval=None
        
    def midpoint(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.nextval is not None and slow is not None:
            fast=fast.nextval.nextval
            slow=slow.nextval
        return slow.data
        
    def loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.nextval is not None and slow is not None:
            fast=fast.nextval.nextval
            slow=slow.nextval
            if slow==fast:
                return True
        return False
            
ll=LinkedList()
ll.insert_at_end("Sat")
#ll.head=Node("Mon")
#ll.head.nextval=Node("Tue")
#ll.head.nextval.nextval=Node("Wed")
#ll.insert_at_head("Sun")
#ll.insert_at_end("Thurs")
ll.printll()

