#리스트 값중 3으로 나눠지고 20보다 작은 수를 출력하는 프로그램

t=[13,21,12,14,30,18]
t.append(27)
print (t)
for x in t:
    if x%3==0 and x<20:
        print (x)
