total = int(input())
num = list(map(int, input().split()))

ans = 0
for data in num:
    count = 0
    if data == 1:
        continue
    else:
        for i in range(2, data+1):
            if data%i == 0:
                count += 1
        if count == 1:
            ans += 1
        
print(ans)
