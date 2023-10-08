N = int(input())

list = []

for i in range(N):
    [name, kor, eng, math] = map(str, input().split())

    list.append([name, int(kor), int(eng), int(math)])

sorted_list = sorted(list, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for score in sorted_list:
    print(score[0])

#sorted 함수를 이용할 때 lambda를 활용하여 정렬 기준을 정해줌

    
