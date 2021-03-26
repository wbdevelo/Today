# 팩토리얼# 팩토리얼
number = int(input())

def factorial(n):
    return n * factorial(n-1) if (n > 1) else 1

print(factorial(number))





# 피보나치 수
num = int(input())

def pibo(n):
    return n if (n<=1) else pibo(n-1)+pibo(n-2)
    
print(pibo(num))
