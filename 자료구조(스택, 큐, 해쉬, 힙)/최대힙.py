# 최대힙은 부모가 자식보다 큰 것을 유지해야함
import sys
# heaqp는 기본적으로 최소힙으로 작동함
import heapq as hq
sys.stdin=open("input.txt", "rt")
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            # -n으로 넣었으니 print할때 마이너스 부호 붙임
            print(-hq.heappop(a))
    else:
        # -n으로 넣어서 최소힙 -> 최대힙으로 만듬
        hq.heappush(a, -n)
