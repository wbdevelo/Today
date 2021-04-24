#1. 백준-동전0(11047)
a, total = map(int, input().split())
coin = []
count = 0
for i in range(a):
    coin.append(input())

for i in reversed(coin):
    count += total // int(i)
    total %= int(i)
    

print(count)



#2. 큰 수의 법칙
n, m ,k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
sum = 0
count = 0

for i in range (m):
    if(count < k):
        sum += li[0]
        count += 1
    else:
        count = 0
        sum += li[1]
        

print(sum)





#3. 백준-ATM(11399)
p = int(input())
time = list(map(int, input().split()))
time.sort(reverse=False)

sum = 0

for i in range(p):
    sum += time[i]
    for j in range(i):
        sum+= time[j]

print(sum)
