N,M = tuple(map(int,input().split()))
A_position = [0]
for _ in range(N):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        A_position.append(A_position[-1] + v)
B_position = [0]
for _ in range(M):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        B_position.append(B_position[-1] + v)
cnt = 0
forward = 0
for i in range(len(A_position)):
    if A_position[i] > B_position[i]:
        if forward != 'A':
            cnt += 1
        forward = 'A'
    elif A_position[i] < B_position[i]:
        if forward != 'B':
            cnt += 1
        forward = 'B'
    else:
        if forward != 0:
            cnt +=1
        forward = 0
print(cnt)