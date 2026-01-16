def s(index,total,arr,result):
    if index>=len(arr):
        result.append(total)
        return
    s(index+1,total+arr[index],arr,result)
    s(index+1,total,arr,result)



arr=[5,9,3]
result = []
s(0,0,arr,result)
print(result)