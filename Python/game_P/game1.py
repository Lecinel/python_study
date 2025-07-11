import random
import time
word_list = ["집에가고싶어요","파이썬","자바","컴퓨터","믹서기","냉장고","칠판","학교","레이더","레코드판","노트북","해외","나라","한국","시나몬","시나브로","케이크","롤케이크","티셔츠","도로","손목터널증후군","필통","샤프","스마트폰","종이","기능사","전기","커피","기술","성능","해돋이","가위","카세트테이프"]

word = random.choice(word_list)
print(word)
start = time.time()
correct = 0
trial = 0
user_msg = ""

while (user_msg != word):
    correct = 0
    user_msg =  input(":")
    for i in range(0,min(len(word),len(user_msg))):
        if word[i] == user_msg[i]:
            correct += 1
    trial += 1

end = time.time()
etime = end - start 
total = max((len(word),len(user_msg)))
accuracy = correct / len(word) * 100
speed = len(user_msg) / etime * 60

print(f"걸린시간{etime:.2F}")
print(f"시도횟수{trial}")
print(f"분당 속도{speed:.2f}")