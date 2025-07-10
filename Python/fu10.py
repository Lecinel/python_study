def test_prime(fin):
    li = []

    for i in range(2, fin+1):
        count = 0 
        for y in range (1,i):
            if i % y == 0:
                count += 1
        if count  < 2:
            li.append(i)
    print(li)

fin = int(input("소수를 판단할 마지막 수를 입력해주세요. : "))

test_prime(fin)