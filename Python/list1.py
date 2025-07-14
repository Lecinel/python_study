def sum_num(innum):
    sum = 0
    for i in range(innum):
        print("점수를 입력해주세요 {0}번째".format(i+1))
        sum += int(input(":"))
    return sum

print("몇 개를 저장하시겠습니까?")

innum = int(input(":"))
print(sum_num(innum))