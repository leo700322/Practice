def C_transform_F():
    while True:
        c = input("Please input the degree Celsius: ")
        try:
            c = float(c)
            break
        except Exception:
            print("Please input digit, thank you.")
    f = (c * 9 / 5) + 32
    print("It is ", f, "degree Fahrenheit.")
    return f
C_transform_F()
