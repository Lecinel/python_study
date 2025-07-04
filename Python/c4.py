hl = int(input("반지름을 입력해주세요"))
PI = 3.141592
if hl < 0:
    print("잘못된값을 입력하셨습니다.")
else:
    print("원의 반지름은 {0}".format(PI*(hl**2)))