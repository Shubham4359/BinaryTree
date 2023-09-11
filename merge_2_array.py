li=[1,3,5,7,9]
vi=[2,4]
mi=[]
i=0
j=0
while i<len(li) and j< len(vi):
    if li[i]<vi[j]:
        mi.append(li[i])
        i+=1
    else:
        mi.append(vi[j])
        j+=1

while i<len(li):
    mi.append(li[i])
    i+=1

while j<len(vi):
    mi.append(vi[j])
    j+=1

print(mi)

