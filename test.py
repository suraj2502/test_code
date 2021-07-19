"""#get the missing numbers from given range of numbers
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
print(result)"""

class get_missing(object):
    def findMissingRanges(self, nums, lower, upper):
        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)
        ranges = []
        pre = lower - 1
        
        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
                
            pre = cur
            
        return ranges


if __name__ == "__main__":

    print (get_missing().findMissingRanges([0, 1, 3, 50, 75], 0, 99))