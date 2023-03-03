print("x,y za prvu")
while True:
    try:
        x1=float(input("x1: "))
        y1=float(input("y1: "))
        break
    except:
        print("Niste upisali broj")
print("x,y za drugu")
while True:
    try:
        x2=float(input("x2: "))
        y2=float(input("y2: "))
        break
    except:
        print("Niste upisali broj")
k=(y2-y1)/(x2-x1)
l=y1-k*x1
print("y={}x{}{}".format(str(k),("+" if l>0 else ""),(str(l) if l!=0 else "")))