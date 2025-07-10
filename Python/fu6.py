import random

c1 = random.randint(0,3)
ch = ""
num1, num2 = map(int,input("숫자 2개를 입력해주세요").split())

collect = 0

if c1 == 0:
    collect = num1 + num2
    ch = "+"
elif c1 == 1:
    collect = num1 - num2
    ch = "-"
elif c1 == 2:
    collect = num1 * num2
    ch = "*"
elif c1 == 3:
    collect = round(num1 / num2,2)
    ch = "/"
else:
    print("문제를 생성중에 오류가 발생하였습니다.")

print("{} {} {} = ?".format(num1,ch,num2))

answer = float(input(" : "))

if answer == collect:
    print("정답입니다.")
else:
    print("답이 아닙니다.")