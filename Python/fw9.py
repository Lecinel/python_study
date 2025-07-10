fibo = int(input("피보나치를 계산할 횟수를 입력해주세요"))
l1 = []
num1 = 1
num2 = 0
temp = 0
count = 0
while count < fibo: # 1 2 3 5 8 
    num2 = num1
    num1 = num2 + temp
    temp = num2
    l1.append(num1)
    count += 1
    
print(l1)
