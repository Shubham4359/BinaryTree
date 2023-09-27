def create_stack():
    st=[]
    return st
    
def push(st,x):
    st.append(x)
    print("pushed element ",x)
    
def size(st):
    return len(st)
    
def is_empty(st):
    if size(st)==0:
        return True
    else:
        return False

def pop(st):
    if is_empty(st)==True:
        return "Pop doesnot exist"
    else:
        st.pop()
        return "Poped out last element"
        
def peek(st):
    if is_empty(st)==True:
        return -1
    else:
        return st[-1]
    
stack=create_stack()
print(pop(stack)," line 32")
push(stack,7)
print(pop(stack)," line 34")
print(peek(stack))
print(is_empty(stack))





    
    
