N,T = tuple(map(int,input().split()))
order_list = list(input())
space = [[ int(x) for x in input().split()] for _ in range(N)]
x,y = N//2,N//2
dxs,dys = [-1,0,1,0],[0,1,0,-1]
move_dir = 0
value_sum = space[x][y]

def in_range(x,y,n):
    return x>=0 and y>=0 and x<n and y<n

for i in order_list:
    if i =='L':
        move_dir = (move_dir+3)%4
    elif i == 'R':
        move_dir = (move_dir+1)%4
    elif i =='F':
        nx,ny = x+dxs[move_dir],y+dys[move_dir]
        if not in_range(nx,ny,N):
            continue
        else:
            x,y = nx,ny
            value_sum += space[x][y]
print(value_sum)