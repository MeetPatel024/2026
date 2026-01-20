nums1 = [4,1,2]
nums2 = [1,3,4,2]
stack = []
ans = dict()
for num in nums2:
    ans[num]=-1

for i in range(len(nums2)-1,-1,-1):
    while len(stack)!=0 and nums2[i]>=stack[-1]:
        stack.pop()
    if stack:
        ans[nums2[i]]=stack[-1]
    stack.append(nums2[i])
result = []
for num in nums1:
    result.append(ans[num])
print(result)