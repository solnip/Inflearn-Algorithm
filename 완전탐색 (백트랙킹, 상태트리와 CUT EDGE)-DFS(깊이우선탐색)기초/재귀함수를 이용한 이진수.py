'''
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용
해서 출력해야 합니다.
'''
import sys
sys.stdin=open("input.txt", "rt")
def DFS(x):
    if x==0:
        # 함수를 종료
        return
    else:
        DFS(x//2)
        print(x % 2, end='')


if __name__=="__main__":
    n=int(input())
    DFS(n)