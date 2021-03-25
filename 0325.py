count = int(input())
stu = 0
ans = []
for i in range(count):
    li = list(map(int, input().split()))
    stu = li[0]
    del li[0]
    
    avg = 0
    for data in li:
        avg += data
    
    avg /= stu
    
    num = 0
    for data in li:
        if data > avg:
            num += 1

    ans.append(num / stu * 100)

for data in ans:
    print("%.3f%%" %data)
