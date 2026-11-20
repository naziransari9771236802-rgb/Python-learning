# Break statement___________

i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1


i = 1

while i <= 20:
    if i == 10:
        break
    print(i)
    i += 1


i = 1

while i <= 30:
    if i > 15:
        break
    print(i)
    i += 1


# Continue Statements______

i = 0

while i < 10:
    i += 1

    if i == 5:
        continue
    print(i)



i = 1

while i <= 20:

    if i == 5 or i == 10:
            i += 1
            continue
    print(i)
    i += 1




i = 1

while i <= 50:
    if i == 10 or i == 20:
        i += 1
        continue

    if i == 30:
        break
    
    print(i)
    i += 1
