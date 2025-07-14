def cal_dic(my_dic):
    sum = 0
    for value in my_dic.values():
        sum += value
    return sum

my_dic = {"옷":100, "컴퓨터":2000, "모니터":320}
print(cal_dic(my_dic))
