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
