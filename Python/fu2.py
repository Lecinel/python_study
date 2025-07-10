def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return round(num1 / num2,2)
def mul(num1, num2):
    return num1 * num2

num1, num2 = map(int,input("값을 2개 입력해주세요").split())

print("합 : ", add(num1,num2), "나누기", div(num1,num2),"빼기",sub(num1,num2),"곱하기",mul(num1,num2))