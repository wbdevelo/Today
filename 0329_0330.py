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

    
    
    
    
4.
count = int(input())
for i in range(count,0,-1):
    print(" "*(count-i) + "*"*i)




5.
count = int(input())
for i in range(1, count+1):
    print(" "*(count-i) + "*"*(2*i-1))




6.
count = int(input())
for i in range(count, 0 , -1):
    print(" "*(count-i) + "*"*(2*i-1))
