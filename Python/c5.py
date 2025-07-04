num1, num2, num3 = map(int,input("숫자 3개를 입력해주세요").split())
if num1 > num2:
    if num1 > num3:
        print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)
     