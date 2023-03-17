hieght = float(input("enter your hieght:"))
wieght= float(input("enter your wieght:"))

m=hieght/100
print(m)
BMI = wieght/(m*m)
print(BMI)

if BMI < 16:
    print("you are extremly thin")
elif BMI< 18.5:
    print("you are thin")
elif  BMI < 25:
    print("you have a good health")
elif  BMI < 30:
    print("you are kind of fat")
else:
    print("you are extremly fat")