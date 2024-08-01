N = int(input())
mirror_space = [list(input()) for _ in range(N)]
start_point = int(input())

def in_range(x,y,n):
    return x>=0 and x<n and y>=0 and y<n

dxs,dys = [0,1,0,-1],[1,0,-1,0]
x,y = 0,0
move_dir = 0
start_dir = 3

for _ in range(start_point-1):
    xn,yn = x+dxs[move_dir],y+dys[move_dir]
    if not in_range(xn,yn,N):
        move_dir = (move_dir+1)%4
        start_dir = (start_dir+1)%4
        continue
    x,y = x+dxs[move_dir],y+dys[move_dir]

progress_dir = (start_dir+2)%4
cnt = 0

while in_range(x,y,N):
    if mirror_space[x][y] == '/':
        if progress_dir == 1:
            progress_dir = 2
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        elif progress_dir == 2:
            progress_dir = 1
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        elif progress_dir == 3:
            progress_dir = 0
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        else:
            progress_dir  = 3
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
    elif mirror_space[x][y] == '\\':
        if progress_dir == 1:
            progress_dir = 0
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        elif progress_dir == 2:
            progress_dir = 3
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        elif progress_dir == 3:
            progress_dir = 2
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
        else:
            progress_dir = 1
            x,y = x + dxs[progress_dir],y+dys[progress_dir]
            cnt += 1
print(cnt)