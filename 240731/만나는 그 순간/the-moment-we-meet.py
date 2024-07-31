N,M = tuple(map(int,input().split()))
A_position = [0]
for _ in range(N):
    d,t = input().split()
    t = int(t)
    if d == 'R':
        for _ in range(t):
            A_position.append(A_position[-1]+1)
    if d == 'L':
        for _ in range(t):
            A_position.append(A_position[-1]-1)
B_position = [0]
for _ in range(M):
    d,t = input().split()
    t = int(t)
    if d == 'R':
        for _ in range(t):
            B_position.append(B_position[-1]+1)
    if d == 'L':
        for _ in range(t):
            B_position.append(B_position[-1]-1)
b = False
for i in range(1,len(A_position)):
    if A_position[i] == B_position[i]:
        print(i)
        b = True
        break
if not b:
    print(-1)