num1 = float(input("실수를 입력해주세요."))
fun = 0
if num1 <= 0:
    fun = num1 ** 2 - (9 * num1) + 2
else: 
    fun = 7 * num1 + 2 
print("함수값은 {0}입니다.".format(fun))

