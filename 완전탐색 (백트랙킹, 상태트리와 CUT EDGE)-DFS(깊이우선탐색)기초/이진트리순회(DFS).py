import sys
sys.stdin=open("input.txt", "rt")
'''
def DFS(v):
    if v>7:
        # 함수를 종료
        return
    else:
        #전우순회
        #자기본연
        print(v, end=' ')
        #왼
        DFS(v*2)
        #오
        DFS(v*2+1)
'''
def DFS(v):
    if v>7:
        # 함수를 종료
        return
    else:
        #중우순회
        #왼
        DFS(v*2)
        # 자기본연
        print(v, end=' ')
        #오
        DFS(v*2+1)
'''
def DFS(v):
    if v>7:
        # 함수를 종료
        return
    else:
        #후우순회
        #왼
        DFS(v*2)
        #오
        DFS(v*2+1)
        # 자기본연
        print(v, end=' ')
        
'''
if __name__=="__main__":
    DFS(1)