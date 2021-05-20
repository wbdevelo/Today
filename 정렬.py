# 선택정렬
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(cards)):
    minNum = cards[i]
    for j in range(i+1, len(cards)):
        if minNum > cards[j]:
            minNum = cards[j]
            cards[j], cards[i] = cards[i], minNum #스와프

print(cards)





# 삽입정렬
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(cards)):
    for j in range(i, 0, -1):
        if cards[j] < cards[j-1]:
            cards[j-1], cards[j] = cards[j], cards[j-1]

print(cards)





# 계수정렬
datas = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0]*(max(datas)+1)

for data in datas:
    count[data] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

        
        
        
        
#1. 위에서 아래로
datas = []
for i in range(4):
    datas.append(int(input()))

datas = sorted(datas, reverse=True)

for data in datas:
    print(data, end=" ")
    
