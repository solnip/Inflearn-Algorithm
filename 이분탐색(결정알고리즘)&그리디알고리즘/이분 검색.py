'''
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.
'''
import sys
sys.stdin=open("input.txt", "rt")
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    #a[mid]값이 m보다 크면 m값이 a[mid]보다 작은쪽에 있다는 뜻이므로
    #rt를 mid-1로 조정
    elif a[mid]>m:
        rt=mid-1
    #a[mid]값이 m보다 작으면 m값이 a[mid]보다 큰쪽에 있다는 뜻이므로
    #lt를 mid+1로 조정
    else:
        lt=mid+1