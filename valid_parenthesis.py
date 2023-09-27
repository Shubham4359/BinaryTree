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
            

print(valid_parenthesis("[{()}]"))
    
    
