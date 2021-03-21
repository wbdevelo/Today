count = input()
data = list(map(int, input().split()))

for i in range(len(data)):
    if data[i] == max(data):
        print(i+1)
        break
