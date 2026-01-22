s = "pwwkew"
left = 0
right = 0
res = 0
dic = dict()

while right<len(s):
    if s[right] in dic:
        left = max(left,dic[s[right]]+1)
    
    res=max(res,right-left+1)
    dic[s[right]]=right
    right+=1

print(res)