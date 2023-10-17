def permutation(freq,temp):
    ok=False
    for i in range(26):
        if freq[i]>0:
            ok=True
    if ok ==False:
        print(temp)
        return
    for i in range(len(freq)):
        if freq[i]>0:
            ok=True
            temp+=chr(i+ord('a'))
            freq[i]-=1
            permutation(freq,temp)
            freq[i]+=1
            temp=temp[0:-1]

s="abc"
n=len(s)
temp=''
freq=[0]*26
for i in range(n):
    x=ord(s[i])-ord('a')
    freq[x]+=1
permutation(freq,temp)
