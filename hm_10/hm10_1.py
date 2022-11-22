def month():
    try:
        s = int(input("month's number: "))
        if s <= 0 or s >= 13:
            raise Exception
        if s == 1:
            print("January")
        elif s == 2:
            print("January")
        elif s == 3:
            print("March")
        elif s == 4:
            print("April")
        elif s == 5:
            print("May")
        elif s == 6:
            print("June")
        elif s == 7:
            print("July")
        elif s == 8:
            print("August")
        elif s == 9:
            print("September")
        elif s == 10:
            print("October")
        elif s == 11:
            print("November")
        elif s == 12:
            print("December")
    except ValueError:
        print ("Wrong! Write a number." )
    except Exception:
        print("You should write number in range 1 - 12")
        month()
month()
