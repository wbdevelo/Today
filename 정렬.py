# 선택정렬
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(cards)):
    minNum = cards[i]
    for j in range(i+1, len(cards)):
        if minNum > cards[j]:
            minNum = cards[j]
            cards[j], cards[i] = cards[i], minNum #스와프

print(cards)
