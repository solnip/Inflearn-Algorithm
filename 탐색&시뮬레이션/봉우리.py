'''
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자
판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개
있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
'''
import sys
sys.stdin = open("input.txt", "rt")
# 상하좌우 탐색은 이런식으로 함
#    좌 상 우 하
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
# 가장자리를 0으로 만들어 주는 방법

# 0번행에 0개의 0으로 초기화된 n개의 값 삽입
a.insert(0, [0]*n)
# 맨 밑에 0으로 초기화된 n개의 값 삽입
a.append([0]*n)
for x in a:
    # 각 행 마다 맨 앞에 0값 삽입
    x.insert(0, 0)
    # 각 행 마다 맨 뒤에 0값 삽입
    x.append(0)
cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all 함수 : 안의 조건이 모두 합이여야 true
        # a[i][j]의 상하좌우 탐색
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            # 이 조건을 만족한다면 봉우리
            cnt+=1
print(cnt)