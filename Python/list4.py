def num_mi(li1):
    print("실행후 {0}".format([-x if x > 2 and x < 9 else x for x in li1 ]))


li1 = [1,2,3,4,5,6,7,8,9,10]
print("실행전 {0}".format(li1))
num_mi(li1)