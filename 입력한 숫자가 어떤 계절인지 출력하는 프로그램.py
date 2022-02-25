#입력한 숫자가 어떤 계절인지 출력하는 프로그램
a = int (input("몇월인지 입력하세요"))
if a == 1 or a == 11 or a ==2:
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
elif a == 9 or a == 10 or a == 11:
    print("fall")
