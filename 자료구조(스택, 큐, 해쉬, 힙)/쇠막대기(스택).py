import sys
sys.stdin=open("input.txt", "rt")
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    # 여는 괄호
    if s[i]=='(':
        stack.append(s[i])
    # 닫는 괄호
    else:
        stack.pop()
        # 레이저 경우
        if s[i-1]=='(':
            # 스택의 길이 누적
            cnt+=len(stack)
        # 쇠막대기의 끝
        else:
            cnt+=1
print(cnt)