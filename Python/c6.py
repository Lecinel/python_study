import random 
computer = random.randint(0,2) # 0 == 가 1 바 2 보
user = input("가위 바위 보")
if user == '가위':
    if computer == 0:
        print("비겼음")
    elif computer == 1:
        print("졌음")
    else:
        print("이겼음")
elif user == '바위':
    if computer == 0 :
        print("이겼음")
    elif computer == 1:
        print("비겼음")
    else:
        print("졌음")
elif user == "보":
    if computer == 0:
        print("졌음")
    elif computer == 1:
        print("이겼음")
    else:  
        print("비겼음") 
else:
    print("잘못된값을 입력했습니다.")

