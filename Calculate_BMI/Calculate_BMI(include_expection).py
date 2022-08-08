def BMI():
    while True:
        h = input("Please input the Height(m): ")
        w = input("Please input the Weight(kg): ") # user input
        try:
            h = float(h) # change user input to interger
            w = float(w)
            break
        except Exception:
            print("Please input the digit, thank you!")
    bmi = w/(h**2)
    print(bmi)
    return bmi
BMI()