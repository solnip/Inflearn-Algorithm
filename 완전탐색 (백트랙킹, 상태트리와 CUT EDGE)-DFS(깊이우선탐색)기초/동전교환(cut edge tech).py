
import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global res
    if sum > m:
        return
    if L > res:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res=21470000
    a.sort(reverse=True)
    cnt=0
    DFS(0, 0)
    print(res)