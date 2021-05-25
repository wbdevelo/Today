# 순차탐색
def sequential(n, array, target):
    for i in range(int(n)):
        if array[i] == target:
            return i+1


n, target = input().split()
array = input().split()

print(sequential(n, array, target))
