import sys
sys.stdin = open("input.txt", "rt")
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
#포인터 변수 0으로 초기화
p1=p2=0
#c라는 빈 리스트 생성
c=[]
#둘중에 하나가 끝까지 가면 끝나는 함수
while p1<n and p2<m:
    #리스트값 비교
    if a[p1]<b[p2]:
        #더 작은 a값 배치
        c.append(a[p1])
        #a의 포인터값 1 증가
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
#위의 while문을 벗어나 p1이 가르키는 값이 n까지 못가고 남은 경우
if p1<n:
    #슬라이스 가능. p1부터 마지막까지 붙여버림
    c=c+a[p1:]
if p2<m:
    #p2부터 끝까지 붙여버림
    c=c+b[p2:]
    for x in c:
        print(x, end = ' ')
