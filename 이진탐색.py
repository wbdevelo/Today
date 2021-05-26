# 순차탐색
def sequential(n, array, target):
    for i in range(int(n)):
        if array[i] == target:
            return i+1


n, target = input().split()
array = input().split()

print(sequential(n, array, target))





# 이진탐색
def binary(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2
    if(array[mid] == target):
        return mid+1
    else:
        if(array[mid] > target):
            return binary(array, target, start, mid-1)
        else:
            return binary(array, target, mid+1, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
