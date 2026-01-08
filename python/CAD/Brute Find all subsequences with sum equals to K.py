def s(ind,sub):
    if ind>=len(nums):
        if sum(sub)==3:
            result.append(sub.copy())
            return
        return
    sub.append(nums[ind])
    s(ind+1,sub)
    sub.pop()
    s(ind+1,sub)
nums = [1,2,3]
k=3
result =[]
s(0,[])
print(result)