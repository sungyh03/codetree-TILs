n,m = tuple(map(int,input().split()))
matrix = [[0 for _ in range(m)] for _ in range(n)]
x,y = 0,0
dxs,dys = [0,1,0,-1],[1,0,-1,0]
move_dir = 0
matrix[x][y] = 'A'
def in_range(x,y,n,m):
    return x>=0 and y>=0 and x<n and y<m
for i in range(1,n*m):
    nx,ny = x+dxs[move_dir],y+dys[move_dir]
    if not in_range(nx,ny,n,m) or matrix[nx][ny] != 0:
        move_dir = (move_dir+1)%4
    x,y = x+dxs[move_dir],y+dys[move_dir]
    matrix[x][y] = chr(ord('A')+i%(ord('Z')-ord('A')+1))
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()