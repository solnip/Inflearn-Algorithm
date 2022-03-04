'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중
가장 큰 합을 출력합니다.
'''
import sys
sys.stdin = open("input.txt", "rt")
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        # i고정 j증가 - 가로줄의 합
        sum1+=a[i][j]
        # i, j 자리바꾸면 - 세로줄의 합
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    #대각선의 합
    sum1+=a[i][i]
    #역대각선의 합
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)