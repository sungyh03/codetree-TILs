n,m = tuple(map(int,input().split()))
x,y = 0,0
dxs,dys=[1,0,-1,0],[0,1,0,-1]
move_dir = 0
matrix = [[0 for _ in range(m)] for _ in range(n)]
matrix[x][y] = 1
def in_range(x,y,n,m):
    return x>=0 and y>=0 and x<n and y<m
for i in range(2,n*m+1):
    nx,ny = x+dxs[move_dir],y+dys[move_dir]
    if not in_range(nx,ny,n,m) or matrix[nx][ny] != 0:
        move_dir = (move_dir+1)%4
    x,y = x+dxs[move_dir],y+dys[move_dir]
    matrix[x][y] = i
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()