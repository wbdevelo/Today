1.
count = int(input())
for i in range(count): 
    print("*"*(i+1))




2.
count = int(input())
for i in range(count):
    space = count-i-1
    print(" "*space + "*"*(i+1))




3.
count = int(input())
for i in range(count, 0,-1):
    print("*"*i)
