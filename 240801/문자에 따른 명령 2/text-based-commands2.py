x,y=0,0
dir_num = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
order_list = list(input())
for i in order_list:
    if i == 'L':
        dir_num = (dir_num+3)%4
    elif i == 'R':
        dir_num = (dir_num+1)%4
    elif i == 'F':
        x,y = x+dx[dir_num],y+dy[dir_num]
print(x,y)