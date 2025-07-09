i = 0


while(i < 5):
    i += 1



print("{}회 반복이 종료됨".format(i))

print("----------------------")


# score = 0
# total_sum = 0
# c = 0
# print("종료할려면 음수값을 입력해주세요.")
# while score >=0:
#     score = int(input("점수를입력해주세요:"))
#     if score >= 0:
#         total_sum += score
#         c += 1 

# if c > 0:
#     average = total_sum / c 
#     print("평균점수는 {0} 입니다.".format(average))

ract = int(input("크기를 입력해주세요"))

for i in range(ract):
    char = ""
    for y in range(ract):
        char += "* "
    print("{0}".format(char))    
