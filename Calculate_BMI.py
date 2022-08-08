def BMI():
    h = float(input("Please input the Height(m): "))
    w = float(input("Please input the Weight: "))
    bmi = w/(h**2)
    print(bmi)
    return bmi
BMI()