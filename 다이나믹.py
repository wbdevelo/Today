#1. 1로 만들기
x = int(input())
d = [0]*30000

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    elif i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    elif i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])





#2. 개미전사
n = int(input())
k = list(map(int, input().split()))
d = [0]*30000

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
