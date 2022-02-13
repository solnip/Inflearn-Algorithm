import sys
#sys.stdin = open("input.txt", "rt")
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    #print(a)
    b=a[s-1:e]
    b.sort()
    print("#%d %d" %(t+1,b[k-1]))