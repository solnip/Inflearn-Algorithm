'''  
창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳
과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.
첫 번째 줄에 창고 가로의 길이인 자연수 L(1<=L<=100)이 주어집니다.
두 번째 줄에 L개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 100을 넘지
않습니다
세 번째 줄에 높이 조정 횟수인 M(1<=M<=1,000)이 주어집니다.
M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.
'''
import sys
sys.stdin=open("input.txt", "rt")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])