a = input().upper()
a_list = list(set(a))

cnt = []
for i in a_list:
    count = a.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(a_list[(cnt.index(max(cnt)))])
    
