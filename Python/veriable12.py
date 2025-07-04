number  = int(input("100000 ~ 999999사이의 숫자를 입력해주세요."))

if(number >= 100000 and number < 1000000):
    fr = number // 1000
    ba = number % 1000
    print(str(fr)+","+str(ba))
else:
    print("숫자가 범위안에 포함되지않음")