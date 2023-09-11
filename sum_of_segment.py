li=[1,3,5,7,9]
x=10
l=0
cur_sum=0
for r in range(0,len(li)):
    cur_sum+=li[r]
    while cur_sum-li[l]>=x:
        cur_sum-=li[l]
        l+=1 
    if cur_sum>=x:
        print(cur_sum,l,r," ")
