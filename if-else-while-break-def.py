a=float(input("number:"))
b=input("action:")
c=float(input("number:"))
if(b=="+"):
    def act():
        print(a+c)
    act()
    while (a+c>0):
        print("above zero")
        break
    else:
        print("below zero")
if(b=="-"):
    def act():
        print(a-c)
    act()
    while (a-c>0):
        print("above zero")
        break
    else:
        print("below zero")
if(b=="*"):
    def act():
        print(a*c)
    act()
    while (a*c>0):
        print("above zero")
        break
    else:
        print("below zero")
if(b=="/"):
    def act():
        print(a/c)
    act()
    while (a/c>0):
        print("above zero")
        break
    else:
        print("below zero")