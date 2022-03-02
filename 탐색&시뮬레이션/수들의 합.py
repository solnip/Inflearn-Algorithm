'''
N개의 수로 된 수열 A[1], A[2], …, A[N]이 있다.이 수열의 i번째 수부터
j번째 수까지의 합 A[i] + A[i + 1] +…+A[j - 1] + A[j]가 M이 되는
경우의 수를 구하는 프로그램을 작성하시오.
 lt rt
  0 1 2 3 4 5 6 7 --> index
a 1 2 1 3 1 1 1 2
- 리스트는 이런식으로 index와 그 값으로 우선 표만들고 시작하기

tot = lt~rt까지의 합
tot < m일때 rt 인덱스 증가
tot = m일때 cnt값 증가
tot > m일때 tot에서 lt값 빼줌 lt는 오른쪽으로 한칸 이동
'''

import sys
sys.stdin = open("input.txt", "rt")
n, m=map(int, input().split())
a=list(map(int, input().split()))
# lt 0 과 rt 1 에서 시작
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        #n보다 작을때까지 더해줌
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    #tot가 m과 같을때는 cnt값 증가
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)