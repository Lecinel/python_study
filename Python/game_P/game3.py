import random
import qrcode

li1 = [["가재는","게 편"],["가는날이","장날이다"],["사공이 많으면","배가 산으로 간다"],["누워서","침 뱉기"],["병 주고","약 준다"],["등잔 밑이","어둡다"],["울며","겨자 먹기"],["원수는","외나무다리에서 만난다."],["마른 하늘에","날벼락"],["티끌 모아","태산"]]
count = 0


def success():
    print("정답입니다.")
    return 1
    
li2 = random.sample(li1,len(li1))

while(len(li2)):
    hint = 0
    first , last = li2.pop()
    img = qrcode.make(first)
    img.save("C:\\Users\\SAMSUNG\\mywork\\python_study\\Python\\game_P\\qrcode.png")
    user_msg = input(":").strip()
    if last == user_msg:
            count += success()
            exitan = input("종료하시겠습니까?(press in your key yes and then exit this game)")
            if exitan == "yes":
                 break
                 
    else:
        print("틀렸습니다.")
        print(last[hint])
        hint += 1
        user_msg = input(":").strip()
        if last == user_msg:
            count += success()
    
      
print("{0}개 맞추셨습니다.".format(count))