#문자열이 저장된 리스트를 만들고 문자열 중에서 "aba"처럼 첫번쨰 문자와 마지막 문자가 동일한 문자열 수를 계산하는 프로그램
def strcount(li1):
    
    count = 0
    for i in li1:
        x = len(i)
        if i[0] == i[x-1]:
            count +=1
    print(count)

li1 = ["aba","cbc","toq","qoa","obo","qoq","cgg",'tot']

strcount(li1)