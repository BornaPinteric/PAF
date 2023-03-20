def pet(n):
    p=5
    for i in range(n):
        p+=1/3
    for i in range(n):
        p-=1/3
    return p
print(pet(200))
print(pet(2000))
print(pet(20000))