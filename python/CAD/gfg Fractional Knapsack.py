val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
arr = []
n = len(val)
res = 0

for i in range(len(val)):
    arr.append((val[i],wt[i]))

# for this above code we can implement
# arr = list(zip(val,wt))

arr.sort(key=lambda x:x[0]/x[1],reverse=True)

for i in range(n):
    if capacity>=arr[i][1]:
        capacity-=arr[i][1]
        res+=arr[i][0]
    else :
        vsause = (capacity*arr[i][0])/arr[i][1]
        res+=vsause
        break
print(res)



