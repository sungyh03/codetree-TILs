x,y = 0,0
dxs,dys = [1,-1,0,0],[0,0,-1,1]
move_dir = -1
dir_dict ={'E':0,'W':1,'S':2,'N':3} 
elapsed_t = 0
arrived = False
N = int(input())
for _ in range(N):
    d,t = input().split()
    t = int(t)
    move_dir = dir_dict[d]
    for _ in range(t):
        x,y = x+dxs[move_dir],y+dys[move_dir]
        elapsed_t += 1
        if x == 0 and y == 0:
            arrived = True
            break
    if arrived:
        break
if elapsed_t != 0:
    print(elapsed_t)
else:
    print(-1)