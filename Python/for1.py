x = 100 
sum = 0
for i in range(x):
    print(x+i)

for y in range(x):
    sum +=x
print(sum)

print("----------------------")

for x in ["장미","가지","동물원",None,"해바라기"]:
    print(x)

print(type(x))

print("----------------------")

for x in "blackpeer":
    print(x)

print("----------------------")

fruits = ["apple","banana","orange","grape","kiwi"]
search_fruit = "orange"

for fruit in fruits:
    print("현재 찾는 과일 {0}".format(fruit))
    if fruit == search_fruit:
        print("찾는 과일 {0} 있습니다.".format(search_fruit))
        break
print("탐색완료")

