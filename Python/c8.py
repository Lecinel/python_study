tall, weight = map(int,(input("키와 몸무게를 입력해주세요").split())) 
stdw = int((tall - 100) * 0.9) #오차 1kg
if stdw < weight:
    print("과체중")
elif stdw > weight:
    print("저체중")
else:
    print("표준")
