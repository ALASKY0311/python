import random
c = 10
win = 0
lose = 0
tie = 0
while True:
    if c == 0:
        print ("game over")
        print ("승:",win,"패:",lose,"무",tie)
        break
    b = ["가위","바위","보"]
    com = random.choice(b)
    a = input("기분나쁜 컴퓨터를 이기기 위해 가위,바위,보중 하나를 골라 입력하세요.")
    print("컴퓨터의결정:",random.choice(b))
    if com == "바위":
        if a == "가위":
            print("컴퓨터한테 지다니.. 불쌍하네요")
            c -= 1
            lose += 1
        if a == "바위":
            print("이겼. 이 아닌 무승부네요 ㅋㅋㅋ")
            c -= 1
            tie += 1
        if a == "보":
            print("이기셨네요 ㅎㅎ 기분좋으시나요?")
            win += 1
    if com == "가위":
        if a == "가위":
            print("사람이면 머리를 사용해서 무승부를 피해보세요")
            c -= 1
            tie += 1
        if a == "바위":
            print("이기셨네요. 이제 실제에서 친구와 함께하는 가위바위보에서나 이기세요.")
            c -= 1
            win += 1
        if a == "보":
            print("컴퓨터한테도 지는 당신은 실제에서 가위바위보를 얼마나 못합니까?")
            c -= 1
            lose +=1
    if com == "보":
        if a == "가위":
            print("축하합니다. 드디어 수많은 컴퓨터와 가위바위보 게임에서 패배한 후 딱 한번 이겼네요")
            c -= 1
            win +=1
        if a == "바위":
            print("패배하셨네요. 시간낭비 하시지 말고 공부하세요.")
            c -= 1
            lose += 1
        if a == "보":
            print("무:무리하지 말고 승:승리하려하지 말고 부: 부모님한테 효도나 하고 여기에 시간낭비하지마세요")
            c -= 1
            tie += 1
            
       


