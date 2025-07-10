li = []

for i in range(2, 21):
    count = 0 
    for y in range (1,i):
        if i % y == 0:
            count += 1
    if count  < 2:
        li.append(i)
print(li)