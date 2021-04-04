#1. 구구단(2739)
dan = int(input())
for i in range(1, 10):
    print("%d * %d = %d" %(dan, i, dan*i))


    
    
    
#2. A+B-3(10950)
count = int(input())
ans = []

for i in range(count):
    ans.append(sum(map(int,input().split())))

for data in ans:
    print(data)

    
    
    

#3. 
last = int(input())
sum = 0
for i in range(1, last+1):
    sum += i

print(sum)
