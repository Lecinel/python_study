numf = int(input("4자리 정수를 입력해주세요."))
# mok = numf // 1000
# numf %= 1000
# mok += numf // 100
# numf %= 100
# mok += numf // 10
# numf %= 10
# mok += numf

mok = 0 
t = 1000

while (t >= 1) :
    mok += numf // t
    numf = numf % t 
    t /= 10

print(mok)