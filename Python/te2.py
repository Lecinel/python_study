# def say_hello(name):
#     print("Hello {0}".format(name))


# say_hello("le")

def my_sum(start,end):
    sum = 0

    for i in range(start, end+1):
        sum += i
    return sum
    
print(my_sum(1,10))
print(my_sum(1,100000))

