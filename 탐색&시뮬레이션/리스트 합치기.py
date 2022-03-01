import sys
#sys.stdin = open("input.txt", "rt")
N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(map(int, input().split()))
c=a+b
c.sort()
for x in c:
    print(x, end=' ')