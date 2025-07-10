def get_int_range(num1, num2, msg):
    tnum = 0
    while(tnum < num1 or tnum > num2):
        print("{}을 입력하시오 {}부터 {}사이의 값".format(msg,num1,num2))
        tnum = int(input(": "))
    return tnum

ch = input("msg를 입력하세요.")
num1, num2 = map(int,input("범위를 입력해주세요").split())
month = get_int_range(num1,num2,ch)
ch = input("msg를 입력하세요.")
num1, num2 = map(int,input("범위를 입력해주세요").split())
day = get_int_range(num1,num2,ch)

