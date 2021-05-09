#1. 게임개발
n, m = input().split()
x, y, d = map(int,input().split())
d_list = [0, 1, 2, 3]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
state = []
for i in range(int(n)):
    state.append(list(map(int, input().split())))

count = 0
for i in range(len(state)):
    for j in range(4):
        if d == d_list[j]:
            d = d_list[0] if j==3 else d_list[j+1]
        if state[i][d] == 0:
            x += dx[d]
            y += dy[d]
            count += 1

print(count)





#2. 왕실의 나이트
data = input()
start = [ord(data[0])-96, int(data[1])]
moves = [
        (2, 1), (-2, 1), (2, -1), (-2, -1),
        (1, 2), (-1, 2), (1, -2), (-1, -2)
        ]
count = 0

for move in moves:
    nx = start[0] + move[0]
    ny = start[1] + move[1]

    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    count += 1

print(count)
