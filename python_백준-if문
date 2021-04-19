#1. 두 수 비교하기(1330)
a, b = map(int, input().split())
if a == b:
    print("==")
else:
    print(">") if a>b else print("<")





#2. 시험 성적(9498)
sc = int(input())
if sc in range(90, 101):
    print("A")
elif sc in range(80, 90):
    print("B")
elif sc in range(70, 80):
    print("C")
elif sc in range(60, 70):
    print("D")
else:
    print("F")
    




#3. 윤년(2753)
year = int(input())
print("1" if (year%4==0)and((year%100!=0)or(year%400==0)) else "0")





#4. 사분면 고르기(14681)
x = int(input())
y = int(input())

print(( (1) if (y>0) else (4) ) if (x>0) else ( (2) if (y>0) else (3) ))





# 알람 시계(2884)
h, m = map(int, input().split())

if m > 44:
    print(h, m-45)
else:
    m = m+15
    
    if h > 0:
        print(h-1, m)
    else:
        print(23, m)
