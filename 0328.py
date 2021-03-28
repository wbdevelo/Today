#모래시계
level = int(input())

for i in range(2*level-1):
    if i < level:
        print(" "*i + "*" * (2*(level-i)-1))
    else:
        space = 2*(i-level+1)
        print(" "*(i-space) + "*" * (space+1))

        
        

#마름모
level = int(input())

for i in range(2*level-1):
    if i < level:
        space = level-i-1
        print(" "*space + "*"*(2*i+1))
    else:
        space = i-level+1
        print(" "*space + "*"*((level-space)*2-1))
