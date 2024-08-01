n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]
answer = 0

def in_range(x,y,n):
    return x>=0 and x<n and y>=0 and y<n

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in zip(dxs,dys):
            xn,yn = i+dx,j+dy
            if in_range(xn,yn,n) and matrix[xn][yn] == 1:
                cnt += 1
        if cnt >= 3:
            answer +=1
print(answer)