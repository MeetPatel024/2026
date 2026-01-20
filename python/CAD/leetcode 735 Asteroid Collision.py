asteroids = [8,-8]
stack = []
for i in range(len(asteroids)):
    curr = asteroids[i]
    if curr<0:
        if asteroids[i]<0:
            while stack and stack[-1]>0 and stack[-1]<=abs(curr):
                stack.pop()
            if stack and stack[-1]==abs(curr):
                stack.pop()
            elif not stack or stack[-1]<0:
                stack.append(curr)
    else:
        stack.append(curr)


print(stack)