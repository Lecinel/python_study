import time
import random

life = 3 
li1 = ["발할라","그리핀","사과","텔레비전","고양이","파이썬","자바","컴퓨터","믹서기","냉장고","칠판","학교","레이더","레코드판","노트북","해외","나라","한국","시나몬","시나브로","케이크","롤케이크","티셔츠","도로","필통","샤프","스마트폰","종이","기능사","전기","커피","기술","성능","해돋이","가위","테이프"]
score = 0
print("게임이 5초후 시작됩니다.")
time.sleep(5)
while(life > 0) :
    start = time.time()
    word = random.choice(li1)
    print(word)
    typing = input(": ")
    end = time.time()
    delay = end - start
    if (word != typing):
        life -= 1
        print("현재 생명 {0}".format(life))
    elif (delay > 2 ):
        life -= 1
        print("현재 생명 {0}".format(life))
    else:
        score += 1
    print("걸린시간 {0:.2f}".format(delay))

print("당신의 점수는 {0}입니다.".format(score))



