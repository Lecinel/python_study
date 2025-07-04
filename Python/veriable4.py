hour, minite = map(int,input("시간과 분을 입력해주세요.").split())
print("초로 변환했을때 {0}초입니다.".format((hour*3600) +(minite * 60)))
