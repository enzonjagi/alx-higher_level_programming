#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = my_list_1 if my_list_1 and type(my_list_1) == list else []
    my_list_2 = my_list_2 if my_list_2 and type(my_list_2) == list else []

    result = 0
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("Wrong type")
        except (ZeroDivisionError, ValueError, TypeError):
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
