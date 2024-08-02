n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
x,y = n//2,n//2
dxs,dys=[0,-1,0,1],[1,0,-1,0]
move_dir = 0
move_num = 1
cnt = 1
matrix[x][y]= cnt
def in_range(x,y,n):
    return x>=0 and y>=0 and x<n and y<n
    
while in_range(x,y,n):
    for _ in range(move_num):
        cnt += 1
        x,y = x+dxs[move_dir],y+dys[move_dir]
        if not in_range(x,y,n):
            break
        matrix[x][y] = cnt
    if move_dir == 1 or move_dir == 3:
        move_num += 1
    move_dir = (move_dir+1)%4


for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()