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
is_forward = -1
for i in range(1,len(A_position)):
    if A_position[i] > B_position[i]:
        if is_forward == 'B' or is_forward == 0:
            cnt += 1
        is_forward = 'A'
    elif A_position[i] < B_position[i]:
        if is_forward == 'A' or is_forward == 0:
            cnt += 1
        is_forward = 'B'
    else:
        is_forward = 0
print(cnt)