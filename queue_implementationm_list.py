def create_queue():
    qu=[]
    return qu
        
def size(qu):
    return len(qu)
    
def is_empty(qu):
    if size(qu)==0:
        return True
    else:
        return False

def enqueue(qu,x):
    qu.append(x)
    return "pushed element in queue"
    
def dequeue(qu):
    if is_empty(qu)==True:
        return "dequeue not possible"
    else:
        qu.pop(0)
        return "dqueue is possible"

def peek(qu):
    if is_empty(qu)==True:
        return -1
    else:
        return qu[0]
        
q=create_queue()
print(enqueue(q,5), 5)
print(enqueue(q,2), 2)
print("top element is ",peek(q))
print(dequeue(q))
print(dequeue(q))
print(dequeue(q))
print(size(q))
print(is_empty(q))


        
        
        
        
        
    
