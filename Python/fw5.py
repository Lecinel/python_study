num1 = int(input("정수를 입력해주세요"))

for i in range(1, num1+1):
    for y in range (i):
        print("*", end=" ")
    print("")
