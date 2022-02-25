#up down 게임
import random

com = random.randint(1,100)
life = 10
while True:
    a = int(input("1부터 100까지숫자를 입력해주세요")) 
    if a == com:
        print("정답입니다.")
        break
    if a >com:
        print ("down")
        
        life -= 1
    if a <com:
        print ("up")
        life -= 1
    if life == 0:
       print ("유다희")
       print("정답은",com,"입니다.")
       break






















