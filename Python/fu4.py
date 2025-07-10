def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
score = int(input("점수를 입력해주세요"))

print("학점 : {0}".format(get_grade(score)))