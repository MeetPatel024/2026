def s(ind,subset):
    if ind>=len(nums):
        result.append(subset.copy())
        return 
    subset.append(nums[ind])
    s(ind+1,subset)
    subset.pop()
    s(ind+1,subset)
nums = [4,5,6]
result = []
s(0,[])
print(result)
