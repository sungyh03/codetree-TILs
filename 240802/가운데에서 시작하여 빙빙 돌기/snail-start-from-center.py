n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
x,y = n-1,n-1
dxs,dys=[0,-1,0,1],[-1,0,1,0]
move_dir = 0
matrix[x][y]=n*n
def in_range(x,y,n):
    return x>=0 and y>=0 and x<n and y<n
for i in range(1,n*n):
    nx,ny = x+dxs[move_dir],y+dys[move_dir]
    if not in_range(nx,ny,n) or matrix[nx][ny] != 0:
        move_dir = (move_dir+1)%4
    x,y = x+dxs[move_dir],y+dys[move_dir]
    matrix[x][y] = n*n-i
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()