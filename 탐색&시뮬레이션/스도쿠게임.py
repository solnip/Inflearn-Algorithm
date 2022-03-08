'''
위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오
고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색
깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES",
잘 못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요.
'''
import sys
#sys.stdin = open("input.txt", "rt")
def check(a):
    # 행과 열을 체크하기 위한 이중 포문
    for i in range(9):
        # 행을 체크하기 위한 ch1
        ch1=[0]*10
        # 열을 체크하기 위한 ch2
        ch2=[0]*10
        for j in range(9):
            # j 가 증가
            # 가로 체크
            ch1[a[i][j]]=1
            # 세로 체크
            ch2[a[j][i]]=1
        # sum함수로 리스트 값들의 합 체크
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    # 그룹 탐색을 위한 사중 포문
    # i가 0, 1, 2
    for i in range(3):
        # j가 0, 1, 2
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")