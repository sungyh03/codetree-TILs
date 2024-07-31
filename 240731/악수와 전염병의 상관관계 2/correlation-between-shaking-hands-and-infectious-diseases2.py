N,K,P,T = tuple(map(int,input().split()))
infected_handshake_cnt = [ 0 for _ in range(N)]
infection = [ 0 for _ in range(N)]
infection[P-1] = 1
infomation = []
for _ in range(T):
    infomation.append(tuple(map(int,input().split())))
infomation.sort()
for _,x,y in infomation:
    if (infection[x-1] == 1 and infected_handshake_cnt[x-1]< K) and (infection[y-1] == 1 and infected_handshake_cnt[y-1]< K) :
        infected_handshake_cnt[x-1]+=1
        infected_handshake_cnt[y-1]+=1
    elif (infection[x-1] == 1 and infected_handshake_cnt[x-1]< K) and infection[y-1] == 0:
        infection[y-1] = 1
        infected_handshake_cnt[x-1]+=1
    elif (infection[y-1] == 1 and infected_handshake_cnt[y-1]< K) and infection[x-1]==0:
        infection[x-1] = 1
        infected_handshake_cnt[y-1]+=1
    elif infection[x-1] == 1 and infection[y-1] == 1:
        infected_handshake_cnt[x-1] += 1
        infected_handshake_cnt[y-1] += 1
    elif infection[x-1] == 1:
        infected_handshake_cnt[x-1] += 1
    elif infection[y-1] == 1:
        infected_handshake_cnt[y-1] += 1
for i in infection:
    print(i,end='')