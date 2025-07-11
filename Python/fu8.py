def getMoneyText(amount):
    return str(amount) + "만원"


amount = 1001
while(amount > 1000 or amount < 0):
    amount = int(input("돈을 입력하시오(단 숫자 1000이하로)"))

print(getMoneyText(amount))