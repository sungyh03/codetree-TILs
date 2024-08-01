N,M = tuple(map(int,input().split()))
space = [[0 for _ in range(N)] for _ in range(N)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]
def in_range(x,y,n):
    return x>=0 and x<n and y>=0 and y<n
for _ in range(M):
    x,y = tuple(map(int,input().split()))
    space[x-1][y-1] = 1
    cnt = 0
    for dx,dy in zip(dxs,dys):
        xn,yn = x-1+dx,y-1+dy
        if in_range(xn,yn,N) and space[xn][yn] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)