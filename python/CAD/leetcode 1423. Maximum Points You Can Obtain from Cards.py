cardPoints = [1,2,3,4,5,6,1] 
k = 3

n= len(cardPoints)
if n==k:
    # return sum(cardPoints) 
    pass

left_sum,right_sum = 0,0
for i in range(0,k):
    left_sum+=cardPoints[i]

maxi = left_sum
right_indx = n-1

for i in range(k-1,-1,-1):
    left_sum -= cardPoints[i]
    right_sum += cardPoints[right_indx]
    maxi = max(maxi,left_sum+right_sum)
    right_indx-=1

print(maxi)