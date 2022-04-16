# 재귀함수와 스택
import sys
sys.stdin=open("input.txt", "rt")
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end=' ')
        # 1 2 3 출력
'''
    if x>0:
        print(x, end=' ')
        DFS(x-1)
        # 3 2 1 출력
'''


if __name__=="__main__":
    n=int(input())
    DFS(n)