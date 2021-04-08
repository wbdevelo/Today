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

    
    
    

#3. 합(8393)
last = int(input())
sum = 0
for i in range(1, last+1):
    sum += i

print(sum)





#4. 빠른 A+B(15552)
import sys

count = int(input())
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)





#5. N찍기(2741)
num = int(input())
for i in range(1, num+1):
    print(i)

    
    
    
    
#6. 기찍N(2742)
print(*range(int(input()),0, -1))





#7. A+B-7(11021)
import sys

num = int(input())
for i in range(1, num+1):
    print("Case #%d: %d" %(i, sum(map(int, sys.stdin.readline().split()))))
