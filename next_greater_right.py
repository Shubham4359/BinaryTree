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
    
def valid_parenthesis(s):
    st=[]
    for i in range(len(s)):
        if s[i]=='('or s[i]=='{' or s[i]=='[':
            st.append(s[i])
        elif s[i]==')':
            if len(st)==0 or st[-1]!='(':
                return False
            else:
                st.pop()
        elif s[i]==']':
            if len(st)==0 or st[-1]!='[':
                return False
            else:
                st.pop()
        elif s[i]=='}':
            if len(st)==0 or st[-1]!='{':
                return False
            else:
                st.pop()
    if len(st)==0:
        return True
    return False
            
def next_greater_right():
    li=[1,7,3,9,12]
    st=create_stack()
    ans=[0]*len(li)
    # direction of movement -> right to left
    for i in range(len(li)-1,-1,-1):
        if is_empty(st)==False and li[i]<peek(st):
            ans[i]=peek(st)
        else:
            while is_empty(st)==False and peek(st)<=li[i]:
                pop(st)
            if is_empty(st)==True:
                ans[i]=-1
            else :
                ans[i]=peek(st)
        push(st,li[i])
    return ans

#print(valid_parenthesis("[{()}]"))
print(next_greater_right())    
    
