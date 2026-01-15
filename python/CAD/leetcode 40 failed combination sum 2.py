def s(index,o,total,candi,result,target):
    if total==target:
        x=o.copy()
        x.sort()
        result.add(tuple(x))
        return
    elif total>=target:
        return
    if index>=len(candi):
        return
    o.append(candi[index])
    s(index+1,o,total+candi[index],candi,result,target)
    o.pop()
    s(index+1,o,total,candi,result,target)


candidates = [10,1,2,7,6,1,5]
target = 8
result=set()
s(0,[],0,candidates,result,target)
s = [list(t) for t in result]
print(s)
