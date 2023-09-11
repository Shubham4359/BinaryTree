li=[1,3,5,7,9]
i=0
j=len(li)-1
x=16
while i<j:
    sum_cur=li[i]+li[j]
    if sum_cur==x:
        print("hehe")
        break
    elif sum_cur>x:
        j-=1
    else:
        i+=1
        
print(i,j)
