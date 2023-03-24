def pet(n):
    p=5
    for i in range(n):
        p+=1.0/3.0
    for i in range(n):
        p-=1.0/3.0
    return p
print("%.15f" % pet(200))
print("%.15f" % pet(2000))
print("%.15f" % pet(20000))