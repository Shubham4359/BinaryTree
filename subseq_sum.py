def subseq(l1,l2,i,cur_sum):
    if i==len(l1):
        print(l2)
        print(cur_sum)
        return
    #ith element-> take it or leave it
    l2.append(l1[i])
    cur_sum+=l1[i]
    subseq(l1,l2,i+1,cur_sum)
    cur_sum-=l1[i]
    l2.pop()
    subseq(l1,l2,i+1,cur_sum)
    
l1=[1,3,9,4]
l2=[]
subseq(l1,l2,0,0)
