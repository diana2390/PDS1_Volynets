list_number = [9, 23, 65, 65, 0]
list_number2 = [1,2,3,4,]
set_list = set(list_number)


def unique_list(a):
    try:
        for i in set_list:
            if a.count(i) > 1:
                raise ValueError
    except ValueError:
        print('List is not unique!')


unique_list(list_number2)
