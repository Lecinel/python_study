while(1):
    ch = ""
    num = int(input("0~20까지의 정수를 입력해주세요"))
    if num >= 0 and num <= 20:
        if num % 3 == 0 :
            ch += "Fizz"
        if num % 5 == 0:
            ch += "Buzz"

        if ch == "":
            print("*")
        else:
            print(ch)
    else:
        print("숫자를 잘못입력했습니다.")