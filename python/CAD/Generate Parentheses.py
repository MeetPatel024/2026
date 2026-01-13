def s(result,l,r,o):
    if l==0 and r==0:
        result.append("".join(o))
        return
    
    if l>0:
        o.append("(")
        s(result,l-1,r,o)
        o.pop()
    
    if r>l:
        o.append(")")
        s(result,l,r-1,o)
        o.pop()
    
    
n = 3
result = []
s(result,n,n,[])
print(result)
