N,M,K = tuple(map(int,input().split()))
penalty_cnt = [0 for _ in range(N)]
penalty_exist = False
for _ in range(M):
    num = int(input())
    penalty_cnt[num-1] += 1
    if penalty_cnt[num-1] == K:
        print(num)
        penalty_exist = True
        break
if not penalty_exist:
    print(-1)