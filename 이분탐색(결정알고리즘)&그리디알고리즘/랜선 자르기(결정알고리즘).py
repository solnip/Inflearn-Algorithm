'''
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이
다. 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을
잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의
랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수
길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때
만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

이분 알고리즘 -> 결정 알고리즘 사용 시 사용
답이 특정 범위 안에 들어있는 문제이면 이분 알고리즘
'''
import sys
sys.stdin=open("input.txt", "rt")
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0
# input이 줄바꿈으로 들어올 때
# 한 개 숫자를 읽고 list에 append
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)