import sys
sys.stdin = open("input.txt", "rt")
# 0부터 20까지 오름차순 배열
a=list(range(21))
# 10개의 줄에
for _ in range(10):
    # 한 줄에 하나씩 10개의 구간이 주어진다
    # s:시작위치 e:끝위치
    s, e=map(int, input().split())
    # 몇바퀴 돌아야되는지
    # 10, 5일때 3바퀴 (10-5+1)//2
    for i in range((e-s+1)//2):
        # a[5+0], a[10-0]=a[10-0], a[5+0]
        a[s+i], a[e-i]=a[e-i], a[s+i]
# 0번 인덱스에 있는 값을 제거시킴
a.pop(0)
# a를 옆으로 줄줄줄 프린트
for x in a:
    print(x, end=' ')
