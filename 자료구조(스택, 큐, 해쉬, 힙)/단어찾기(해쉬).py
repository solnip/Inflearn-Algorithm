'''
현수는 영어로 시는 쓰는 것을 좋아합니다.
현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다. 
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.
여러분이 찾아 주세요.
'''
import sys
sys.stdin=open("input.txt", "rt")
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items():
    # value가 1인 key print
    if val==1:
        print(key)
        break