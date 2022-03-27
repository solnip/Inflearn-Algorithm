'''
정보 왕국의 이웃 나라 외동딸 공주가 숲속의 괴물에게 잡혀갔습니다.
정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 합니다. 정보왕국의 왕은
다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했습니다.
왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다. 그리고 1번 왕자부터 N
번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다. 그리고 1번 왕자부터 시
계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다. 한 왕자가 K(특정숫자)를 외치면 그
왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다. 그리고 다음 왕자부터 다시
1부터 시작하여 번호를 외친다.
이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있다.
'''
import sys
# queue쓰려면 deque import해야함
from collections import deque
sys.stdin=open("input.txt", "rt")
n, k=map(int, input().split())
dq=list(range(1, n+1))
dq=deque(dq)
while dq:
    for _ in range(k-1):
        # 맨 앞 숫자를 pop해서 뒤에 append
        cur=dq.popleft()
        dq.append(cur)
    # k번째 사람은 pop만 --queue에서 사라짐
    dq.popleft()
    # queue에서 한명이 남았으면 출력
    if len(dq)==1:
        print(dq[0])
        # break도 가능
        # dq를 0으로 만들어서 while문 멈춤
        dq.popleft()
