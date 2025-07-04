num1, num2 = map(int,input("정수 두 개를 입력해주세요. : ").split())
print("정수의 합: {0} 차: {1} 곱: {2} 평균: {3} 큰수: {4} 작은수: {5}".format(num1 + num2, num1 - num2, num1 * num2, (num1 + num2)/2, max(num1, num2), min(num1, num2)))    
