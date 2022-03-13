'''
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마
구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
값을 출력하는 프로그램을 작성하세요.
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩
주어집니다.
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
'''
import sys
sys.stdin=open("input.txt", "rt")
def Count(len):
    # 처음에 말을 한마리 배치한다
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        # 말을 배치하려는 지점과 전에 배치한 말의 거리가 len보다 크면 if문 돔
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt
n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
# lt는 두 말의 가능한 가장 가까운 거리
# rt는 두 말의 가능한 가장 먼 거리
# mid 답을 찾는 값 = 가장 가까운 두 말의 최대 거리
# 1, 9이면 mid = 5
# mid가 5일때 놓을 수 있는 말의 수는 2마리. 3마리를 놔야하므로 rt-1
lt=1
rt=Line[n-1]
res=0
while lt<rt:
    mid=(lt+rt)//2
    # 놓을 수 있는 말의 수 Count(mid)가 c보다 크거나 같으면 답
    # 더 먼 거리도 되는지 lt값 늘려봄
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
