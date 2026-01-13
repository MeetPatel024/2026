def s(index,total,result,o,candi,target):
    if total>=target:
        if total==target:
            result.append(o.copy())
        return
    if index>len(candi)-1:
        return
    o.append(candi[index])
    s(index,total+candi[index],result,o,candi,target)
    e = o.pop()
    s(index+1,total,result,o,candi,target)


candidate = [2,3,6,7]
target = 7
result = []
s(0,0,result,[],candidate,target)
print(result)

