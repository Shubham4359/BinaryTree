li=[[35,37,41,40],[36,38,33,42],[35,35,34,30],[28,39,35,34],[24,49,51,27]]
# [38.25, 37.25, 33.5, 34.0, 37.75]
# 5 days -> i need to find the coldest day in town
# instead of the day min temp is coming we want the slot in which avg temp occurs?
min_day=-1
min_temp=100000
for i in range(len(li)):
    sum1=0
    for c in range(len(li[i])):
        sum1+=li[i][c]
    sum1=sum1/len(li[i])
    if min_temp>sum1:
        min_temp=sum1
        min_day=i

print(min_temp)
print(min_day+1)
        
li=[[35,37,41,40],[36,38,33,42],[35,35,34,30],[28,39,35,34],[24,49,51,27]]
# [38.25, 37.25, 33.5, 34.0, 37.75]
# 5 days -> i need to find the coldest day in town
# instead of the day min temp is coming we want the slot in which avg temp is minimum?
# min temp at any day any slot

min_day=-1
min_temp=100000
# no of slots
for i in range(len(li[0])):
    sum1=0
    for c in range(len(li)):
        sum1+=li[c][i]
    sum1=sum1/len(li)
    if min_temp>sum1:
        min_temp=sum1
        min_day=i

print(min_temp)
print(min_day+1)
        

min_temp=100000
# no of slots
for i in range(len(li)):
    for c in range(len(li[i])):
        min_temp=min(min_temp,li[i][c])
        
print(min_temp)
