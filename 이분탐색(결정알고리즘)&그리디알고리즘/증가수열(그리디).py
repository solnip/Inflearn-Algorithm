'''
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열
을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니
다.
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4,
왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있습니다.
'''
import sys
sys.stdin=open("input.txt", "rt")
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
# lt         rt 포인터 둠
# 2  4  5  1  3
# last보다 lt, rt가 크므로
# (2,L) (3,R) 튜플 형식으로 대고 더 작은 값인 2 선택 -> last로 삽입
last=0
# 문자열 넣을 변수
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    # 아무값도 들어가지 않은 경우
    if len(tmp)==0:
        break
    else:
        # 0번은 제일 첫번째 값을 뜻하고 1번은 tuple값에서 위치(L/R)을 뜻함
        res=res+tmp[0][1]
        last=tmp[0][0]
        # tmp에 L이 들어간 경우 lt 포인터를 오른쪽으로 이동
        if tmp[0][1]=='L':
            lt+=1
        # R이 들어간 경우 rt 포인터를 왼쪽으로 이동
        else:
            rt-=1
    tmp.clear()
#문자열의 길이가 바로 수열의 길이
print(len(res))
print(res)
    