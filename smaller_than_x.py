li=[1,2,3,4,5,6,7,8,9,10]
l=0
r=len(li)-1
# last element smaller than or equal to x 
x=4
while (r-l)>1:
    mid=(l+r)//2
    if li[mid]<=x:
        l=mid 
    elif li[mid]>x:
        r=mid

print(l)
