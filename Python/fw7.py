num = int(input("정수를 입력해주세요."))
sum = 0

for i in range(1,num+1):
    sum += i ** 2

print("합은 {0}".format(sum))
