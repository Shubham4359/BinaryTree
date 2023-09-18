li=[0,0,0,0,0,0,1,1,1,1,1,1]
l=0
r=len(li)-1
while (r-l)>1:
    mid=(l+r)//2
    if li[mid]==0:
        l=mid 
    elif li[mid]==1:
        r=mid

print(l)
