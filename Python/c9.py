import random
l1 = ["+","-","*","/"]
s1 = random.randint(0,3)
num1 = random.randint(0,2000)
num2 = random.randint(0,2000)
answer = 0
if l1[s1] == "+":
    answer = num1 + num2
elif l1[s1] == "-":
    answer = num1 - num2
elif l1[s1] == "*":
    answer = num1 * num2
elif l1[s1] == "/":
    if num1 == 0 or num2 == 0:
        print("값이 0이 나왔습니다. 다시 실행해주세요.")
    else:
        answer = round(num1 / num2,2)
else:
    print("뭔가 잘못되었습니다.")

print("{0} {1} {2} = ?".format(num1,l1[s1],num2))

uanswer = int(input(": "))
print(answer)
if answer == uanswer:
    print("정답입니다.")
else:
    print("못맞춤")
