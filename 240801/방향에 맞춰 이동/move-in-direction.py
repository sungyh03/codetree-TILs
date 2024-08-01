N = int(input())
x,y = 0,0
dx,dy = [1,-1,0,0],[0,0,-1,1]
for _ in range(N):
    direction,distance = input().split()
    distance = int(distance)
    if direction == 'E':
        x,y = x+(dx[0]*distance),y+(dy[0]*distance)
    elif direction == 'W':
        x,y = x+(dx[1]*distance),y+(dy[1]*distance)
    elif direction == 'S':
        x,y = x+(dx[2]*distance),y+(dy[2]*distance)
    elif direction == 'N':
        x,y = x+(dx[3]*distance),y+(dy[3]*distance)
print(x,y)