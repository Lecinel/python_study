size = int(input("리스트의 크기를 정해주세요"))
li1 = []
li2 = []
s = False

def sT(li1,li2):
    s = False
    for i in li1:
        if i in li2:
            s = True
    return s

print("첫번쨰 리스트를 입력해주세요")
for i in range(size):
    li1.append(input(":"))
print("두번쨰 리스트를 입력해주세요")
for y in range(size):
    li2.append(input(":"))
s = sT(li1,li2)

if(s):
    print("같은것이 있습니다.")
else:
    print("같은것이 없습니다.")




