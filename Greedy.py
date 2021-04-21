#1. 백준_동전0(11047)
a, total = map(int, input().split())
coin = []
count = 0
for i in range(a):
    coin.append(input())

for i in reversed(coin):
    count += total // int(i)
    total %= int(i)
    

print(count)
