nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

l = 0
r = 0
zero = 0
maxi=0
for r in range(len(nums)):
    if nums[r]==0:
        zero+=1
    while zero>k:
        if nums[l]==0:
            zero-=1
        l+=1
    if zero<=k:
        maxi=max(r-l+1,maxi)
    

print(maxi)