n = int(input())
list = []

for i in range(n):
    [a,b] = map(int, input().split())
    list.append([a,b])

list.sort()

for i in list:
    print(i[0], i[1])

#sort 함수 오름차순으로, 앞 순서부터 정렬
