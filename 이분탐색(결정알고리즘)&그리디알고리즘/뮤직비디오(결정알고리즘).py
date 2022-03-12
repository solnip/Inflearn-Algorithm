'''
지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지
되어야 한다. 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다. 즉, 1번 노래와 5번
노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야
한다. 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는
DVD를 가급적 줄이려고 한다. 고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기
로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 그리고 M개의 DVD는
모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.
첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 다음 줄에는 조영필이 라이브에서
부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다. 부른 곡의 길이는 10,000분을
넘지 않는다고 가정하자.
첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.
'''
import sys
sys.stdin=open("input.txt", "rt")
def Count(capacity):
    # 일단 dvd 1장이 필요함
    cnt=1
    sum=0
    for x in Music:
        # sum은 누적된 곡의 시간
        # 새로운 곡의 시간
        # if 이 곡도 저장할 수 있냐
        if sum+x>capacity:
            # 없으면 dvd 한 장 추가
            cnt+=1
            # sum도 x로 새로 초기화
            sum=x
        else:
            # 저장 가능하면 새로운 곡도 누적함
            sum+=x
    # dvd의 값 return
    return cnt

n, m=map(int, input().split())
res=0
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
while lt<=rt:
    # dvd의 용량 = mid
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        # 이 용량으로 dvd에 m장 이하로 저장 가능하므로
        # 일단 res에 mid 저장
        res=mid
        # 얼마나 더 줄일 수 있는지 rt도 1 줄여서 다시 해봄
        rt=mid-1
    else:
        # 용량이 너무 작아서 더 큰게 필요하다는 뜻
        # lt의 값 늘려줌
        lt=mid+1
print(res)