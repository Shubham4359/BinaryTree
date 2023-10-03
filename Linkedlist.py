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
            print(start.data)
            start=start.nextval
            
ll=LinkedList()
ll.head=Node("Mon")
t1=Node("Tue")
ll.head.nextval=t1
t2=Node("Wed")
t1.nextval=t2
#ll.printll()
l1=LinkedList()
l1.head=t2
l1.head.nextval=ll.head
t1.nextval=None
l1.printll()


