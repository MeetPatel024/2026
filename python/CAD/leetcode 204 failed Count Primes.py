def s(n, result):
    for i in range(2, n):  
        is_prime = True
        j = 2
        
        while j * j <= i:
            if i % j == 0:
                is_prime = False
                break
            j += 1
        
        if is_prime:
            result.append(i)

n = 10
result = []
s(n, result)
print(result)
