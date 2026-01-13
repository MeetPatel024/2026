def s(index,flag,numbers,result):
    if index>=len(numbers):
        result.append("".join(numbers))
        return
    numbers[index]="0"
    s(index+1,True,numbers,result)
    if flag==True:
        numbers[index]="1"
        s(index+1,False,numbers,result)
        numbers[index]="0"

N = 3
numbers = ["0"]*N
result = []
s(0,True,numbers,result)
print(result)





"""
class Solution:
    
    def s(self,index,flag,numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"   
        self.s(index+1,True,numbers,result)
        if flag==True:
            numbers[index]="1"
            self.s(index+1,False,numbers,result)
            numbers[index]="0"
            
    
    def binstr(self, n):
        nums = ["0"]*n    
        result = []
        self.s(0,True,nums,result)

        return result
"""