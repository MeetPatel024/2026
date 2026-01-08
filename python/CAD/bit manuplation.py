def convert_to_binary(x):
    stack = []
    o = []
    while x>=1:
        remainder = x%2
        stack.append(remainder)
        x = x//2
    while stack:
        o.append(stack.pop())
    return o

def convert_to_int(arr):
    n = len(arr)-1
    o = 0
    for i in arr:
        if i==1:
            c = 2**n
            o = o+c
        n-=1
    return o

ans = convert_to_binary(1231)
print(ans)
ans2 = convert_to_int(ans)
print(ans2)
