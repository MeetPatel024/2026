s = "aab"
#output = 3 (wke)
lis =[]
count = 0
res = 0
for i in range(len(s)):
    if not lis:
        lis.append(s[i])
        count+=1
    elif lis and s[i] not in lis:
        lis.append(s[i])
        count+=1
    elif s[i] in lis:
        while s[i] in lis:
            lis.pop(0)
            count-=1
        lis.append(s[i])
        count+=1
    res = max(res,count)

print(res)