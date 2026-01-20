def solve(nums,ans):
    stack = []
    nums = nums[::-1]
    for i in range(len(nums)):
        while len(stack)!=0 and stack[-1]<nums[i]:
            stack.pop()
        if not stack:
            stack.append(nums[i])
            continue
        ans[i]=stack[-1]
        stack.append(nums[i])
    print(ans[::-1])
        

nums = [19,2,4,9,3,5,8,10]
ans = [-1]*len(nums)
solve(nums,ans)
