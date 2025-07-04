import math
x1, y1, x2, y2 = map(int,input("좌표값 x1, y1, x2, y2를 입력해주세요.").split())
print(math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)))