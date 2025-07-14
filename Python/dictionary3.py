def findkey(num):
    d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
    if d.get(num):
        print("있습니다.")
    else:
        print("없습니다.")

num = int(input("찾는 키값을 입력해주세요"))
findkey(num)