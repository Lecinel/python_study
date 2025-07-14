def make_dict(li1,li2):
    dic = {}
    for i in range(len(li1)):
        dic[i] = li2[i]
    return dic

li1 = [1,2,3,4,5]
li2 = [10,20,30,40,50]

dict1 = make_dict(li1,li2)

print(dict1)