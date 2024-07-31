n,m = tuple(map(int,input().split()))
A_position = [0]
for _ in range(n):
    t,d = input().split()
    t = int(t)
    if d == 'R':
        for _ in range(t):
            A_position.append(A_position[-1] + 1)
    if d == 'L':
        for _ in range(t):
            A_position.append(A_position[-1] - 1)
B_position = [0]
for _ in range(m):
    t,d = input().split()
    t = int(t)
    if d == 'R':
        for _ in range(t):
            B_position.append(B_position[-1] + 1)
    if d == 'L':
        for _ in range(t):
            B_position.append(B_position[-1] - 1)
if len(A_position)>len(B_position):
    for _ in range(len(A_position)-len(B_position)):
        B_position.append(B_position[-1])
if len(A_position)<len(B_position):
    for _ in range(len(B_position)-len(A_position)):
        A_position.append(A_position[-1])
cnt = 0
for i in range(1,len(A_position)-1):
    if A_position[i] != B_position[i] and A_position[i+1] == B_position[i+1]:
        cnt += 1
print(cnt)