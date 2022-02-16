import sys
#sys.stdin = open("input.txt", "rt")
n, m=map(int, input().split())
cnt=[0]*(n+m+3)
max=-2147000000
#주사위의 합 나올때마다 인덱스에 1추가
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1
#max값 지정
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
#max값 나오는 인덱스 출력
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
