def F_transform_C():
    while True:
        f = input("Please input the degree Celsius: ")
        try:
            f = float(f)
            break
        except Exception:
            print("Please input digit, thank you.")
    c = 5 / 9 * (f-32)
    print("It is ", c, "degree Fahrenheit.")    
    return c
F_transform_C()