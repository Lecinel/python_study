def sortlist(li1):
    li1 = sorted(set(li1))

    return li1

li1 = list(map(int,input("정수 리스트를 입력해주세요: ").split()))

print(sortlist(li1))