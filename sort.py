def bubble_sort(a):
    n=len(a)
    for i in range(n):
        is_swaped=False
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                is_swaped=True
                a[j],a[j+1]=a[j+1],a[j]
        if is_swaped == False:
            break

def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1 
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        
        
if __name__=="__main__":
    li=[2,1,3,-4,6,3]
    insertion_sort(li)
    print(li)
#    [-4, 1, 2, 3, 3, 6]
