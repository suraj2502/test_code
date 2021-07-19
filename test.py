#get the missing numbers from given range of numbers
def get_missing(a,n,l,h):
    s=set(a)
    result=[]
    for i in range(l,h+1):
        if i not in s:
            result.append(i)
    return result


#driver code for get_missing function
a=[0, 1, 3, 50, 75]
n=len(a)
l=0
h=99
result= get_missing(a,n,l,h)
print(result)