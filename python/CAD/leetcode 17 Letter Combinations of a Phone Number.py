def s(index,o,sub):
    if index>=len(digits):
        sub.append("".join(o.copy()))
        return
    for i in arr[digits[index]]:
        o.append(i)
        s(index+1,o,sub)
        o.pop()





arr = {"2":"abc",
       "3":"def",
       "4":"ghi",
       "5":"jkl",
       "6":"mno",
       "7":'pqrs',
       "8":'tuv',
       "9":'wxyz'}
digits = "234"
sub = []
s(0,[],sub)
print(sub)