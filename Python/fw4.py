num = int(input("정수를 입력해주세요"))

for i in range(1,num+1):
    if num % i == 0: 
        print(i)
    