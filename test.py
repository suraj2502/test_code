def get_missing(a,n,l,h):
    s=set(a)
    result=[]
    for i in range(l,h+1):
        if i not in s:
            result.append(i)
    return result

a=[0, 1, 3, 50, 75]
n=len(a)
l=0
h=99
result= get_missing(a,n,l,h)
print(result)