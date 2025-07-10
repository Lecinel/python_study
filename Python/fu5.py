def checkPass(p):
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    for i in p:
        if check1 == False:
            check1 = i.islower()
        if check2 == False:
            check2 = i.isupper()
        if check3 == False:
            check3 = i.isdigit()

    if len(p) >= 8:
        check4 = True
    
    if check1 and check2 and check3 and check4:
        print("패스워드를 생성할 수 있습니다.")
    else:
        print("패스워드가 이상합니다.")  
    

p = input("패스워드를 입력해주세요")
checkPass(p)
