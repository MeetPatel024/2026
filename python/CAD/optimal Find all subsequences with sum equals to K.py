def s(ind,total,sub):
    global count
    if total>k:
        return
    if ind>=len(nums):
        if total==3:
            result.append(sub.copy())
            count +=1
            return
        return
    sub.append(nums[ind])
    sum = total+nums[ind]
    s(ind+1,sum,sub)
    e = sub.pop()
    sum = total
    s(ind+1,sum,sub)

nums = [1,2,3]
k=3
count = 0
result = []
s(0,0,[])
print(result)
print(count)