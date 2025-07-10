import fu2

def calc(num1,num2):
    print("합 : {0} 차: {1} 곱 : {2} 나눗셈: {3}".format(fu2.add(num1,num2),fu2.sub(num1,num2),fu2.mul(num1,num2),fu2.div(num1,num2)))

num1, num2 = map(int,input("값을 2개 입력해주세요").split())