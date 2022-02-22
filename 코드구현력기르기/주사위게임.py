import sys
sys.stdin = open("input.txt", "rt")

N=int(input())
max = -21470000

for i in range(N):
    tmp=input().split()
    tmp.sort()
    a, b, c=map(int, tmp)
    #if문은 제일 좋은것부터 시작
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money>max:
        max=money

print(max)