num1, num2 = map(int,input("정수 두개를 입력해주세요.").split())

maxdiv = 0
max = num1
if num1 < num2:
    max = num2
for i in range(1,max):
    if num1 % i == 0 and num2 % i == 0:
        maxdiv = i

print (maxdiv)