mane_function():
    s = int(input("month: "))
    if s == 12 or s == 1 or s == 2 :
        print("winter")
    elif s >= 3 and s <= 5:
        print("spring")  
    elif s >= 6 and s <= 8:
        print("summer")