'''
유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고
있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는
프로그램을 작성하세요.
'''
import sys
# deque라는 자료구조
# list는 pop할때마다 재정렬해서 비효율적
# deque는 pop해도 재정렬안함 조금 더 효율적
from collections import deque
sys.stdin=open("input.txt", "rt")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    # 리스트 p의 길이가 1이면 남은자료가 1이라는 뜻
    if len(p)==1:
        # 한명 남았으면 혼자 타고 나가고 break로 while문 탈출하면 됨
        cnt+=1
        break
    # 맨마지막 자료는 p[-1]
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        # 제일 앞의 자료
        p.popleft()
        # 제일 마지막 자료
        p.pop()
        cnt+=1
print(cnt)