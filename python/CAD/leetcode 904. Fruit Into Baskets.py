fruits=[3,3,3,1,2,1,1,2,3,3,4]

max_len=0
mydict = dict()
r = 0
l = 0

while r<len(fruits):
    mydict[fruits[r]]=mydict.get(fruits[r],0)+1
    if len(mydict)>2:
        mydict[fruits[l]]-=1
        if mydict[fruits[l]]==0:
            del mydict[fruits[l]]
        l+=1
    if len(mydict)<3:
        max_len = max(r-l+1,max_len)
    r+=1

print(max_len)