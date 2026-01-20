nums = [1,2,3,4,3]
stack = []
ans = [-1]*len(nums)
for i in nums[::-1]:
    stack.append(i)

for i in range(len(nums)-1,-1,-1):
    while len(stack)!=0 and nums[i]>=stack[-1]:
        stack.pop()
    if stack:
        ans[i]=stack[-1]
    stack.append(nums[i])
print(ans)
