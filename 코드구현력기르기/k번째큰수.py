import sys
#sys.stdin = open("input.txt", "rt")
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set()
#set이라는 자료구조는 중복을 제거한다
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
#set은 sort기능없어서 다시 list화 해줘야함
res=list(res)
#내림차순정렬
res.sort(reverse=True)
print(res[k-1])