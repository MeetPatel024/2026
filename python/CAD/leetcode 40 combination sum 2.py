def s(index,total,sub):
    if total ==0:
        result.append(sub.copy())
        return
    if total<0:
        return
    if index>=len(nums):
        return
    for i in range(index,len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue
        sub.append(nums[i])
        sum = total-nums[i]
        s(i+1,sum,sub)
        sub.pop()

nums = [1,1,1,2,3]
target = 3
nums.sort()
result= []
s(0,target,[])
print(result)