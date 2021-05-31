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

    
    
    
    
# 부품찾기_이진
n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def find(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return "yes"
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1

    return None

for target in targets:
    result = find(array, target, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

        
        
        
        
        
# 부품찾기_계수정렬1
n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

countArray = [0]*(max(array)+1)
for target in targets:
    for data in array:
        if target == data:
            countArray[target] += 1

for target in targets:
    if countArray[target] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")

        
        
        
# 부품찾기_계수정렬2
n = int(input())
array = [0]*1000000

for i in input().split():
    array[int(i)] += 1

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if array[target] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")

        
        
        
        
        
# 떡볶이 떡 찾기
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def make(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for rice in array:
            if rice >= mid:
                sum += rice - mid
        if sum == target:
            return mid
        elif sum > target:
            return make(array, target, mid+1, end)
        else:
            return make(array, target, start, mid-1)
            


print(make(array, target, min(array), max(array)))



