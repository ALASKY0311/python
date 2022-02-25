#장애물 먹는 프로그램, 점수 출력
import pygame as p
import random as r
a = 1


p.init() #파이게임 초기화 기능
sc = p.display.set_mode([700,700]) #해상도 설정 [가로크기,세로크기]
p.display.set_caption("이미지 움직이기") #게임 창 이름 설정
#1.이미지 불러오기
image = p.image.load("12345.png")
image2 = p.image.load("hello.png")
#2.이미지 객체화
i_rect = image.get_rect(left =200, top = 200) #left = x좌표,top = y좌표
i_rect2= image2.get_rect(left =400, top = 200)
print(i_rect)
playing = True

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()
            playing =False
    if event.type == p.KEYDOWN:
        if event.key == p.K_UP:
            i_rect.top-=1
        if event.key == p.K_DOWN:
            i_rect.top+=1
        if event.key == p.K_LEFT:
            i_rect.left-=1
        if event.key == p.K_RIGHT:
            i_rect.left+=1
    sc.fill((255,255,255))
    sc.blit(image,i_rect)
    sc.blit(image2,i_rect2)
    if i_rect.colliderect(i_rect2): #좌표변수.colliderect(충돌좌표변수)
        i_rect2.left= r.randint(1,650)
        i_rect2.top= r.randint(1,650)
        a +=1
        print ("점수는:",a)
    p.display.flip()
