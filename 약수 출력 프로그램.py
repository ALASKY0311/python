#약수 출력 프로그sheep고기 맛있다
a = int(input("숫자를 입력해주시면 약수를 출력해드립니다."))
for x in range(1,101,1):
    if a%x== 0:
        print(x)
