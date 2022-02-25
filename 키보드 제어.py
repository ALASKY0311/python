#키보드 제어 프로그램
import pygame as p
x = 0
y = 0
p.init() #파이게임 초기화 기능
sc = p.display.set_mode([700,700]) #해상도 설정 [가로크기,세로크기]
p.display.set_caption("키보드 제어") #게임 창 이름 설정
#이미지 불러오기
playing = True
# 1.이미지 불러오기
image = p.image.load("12345.png")
while playing:
    for event in p.event.get(): #사용자가 어떤걸 눌렀는지 감지
        if event.type == p.QUIT: #파이게임 x버튼을 눌렀을떄
            p.quit() #파이게임 끄는 명령어
            quit() #shell(결과창) 끄는 명령어
            playing = False #실행중인 게임을 멈추는 명령어
    if event.type == p.KEYDOWN: # 키보드를 눌렀을떄
        if event.key == p.K_UP: #위쪽 키보드를 눌렀을떄
            y -= 1
            sc.fill([255,0,0])
            p.display.flip()
        if event.key == p.K_DOWN:#아래쪽 키보드를 눌렀을때
            y += 1
            sc.fill([0,0,255])
            p.display.flip()
        if event.key == p.K_LEFT: #위쪽 키보드를 눌렀을떄
            x -= 1
            sc.fill([255,255,0])
            p.display.flip()
        if event.key == p.K_RIGHT: #아래쪽 키보드를 눌렀을때
            x += 1
            sc.fill([0,255,0])
            p.display.flip()
    if event.type == p.KEYUP:#키보드를 때었을때
        sc.fill([255,255,255])
        p.display.flip()
    
# 2.이미지 화면 업로드
    sc.blit(image,[x,y]) #sc.blit(이미지변수이름,좌표값[x,y])
    p.display.flip() #화면 업데이트
    
