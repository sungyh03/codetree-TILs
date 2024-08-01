n,t = tuple(map(int,input().split()))
r,c,d = input().split()
x,y = int(r),int(c)
dxs,dys = [0,1,-1,0],[1,0,0,-1]
dir_dict = {'U':2,'D':1,'R':0,'L':3}
move_dir = dir_dict[d]
def in_range(x,y,n):
    return x>0 and x<=n and y>0 and y<=n
for _ in range(t):
    nx,ny = x+dxs[move_dir],y+dys[move_dir]
    if not in_range(nx,ny,n):
        move_dir = 3-move_dir
    else:
        x,y = nx,ny
print(x,y)