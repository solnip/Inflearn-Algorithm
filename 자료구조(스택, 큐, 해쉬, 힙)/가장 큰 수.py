''' 
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하
여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는
유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.
'''
# 스택은 Last In First Out
# pop append
import sys
sys.stdin=open("input.txt", "rt")
num ,m=map(int, input().split())
# str처리 해줘야 숫자 하나하나에 접근 가능
num=list(map(int, str(num)))
stack=[]
for x in num:
    # stack 맨 상단 값이 놓여질 값보다 작으면 pop
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
for x in stack:
    print(x, end='')
