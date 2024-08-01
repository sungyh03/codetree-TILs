x,y = 0,0
order_list = list(input())
move_dir = 0
dxs,dys = [0,1,0,-1],[1,0,-1,0]
elapsed_time = 0
arrived = False
for i in order_list:
    if i == 'L':
        move_dir = (move_dir+3)%4
    elif i == 'R':
        move_dir = (move_dir+1)%4
    elif i =='F':
        x,y = x+dxs[move_dir],y+dys[move_dir]
    elapsed_time += 1
    if x == 0 and y == 0:
        arrived = True
        break
if arrived:
    print(elapsed_time)
else:
    print(-1)