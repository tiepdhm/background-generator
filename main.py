def divide(num1, num2):
    try:
        if (num1 and num2) or (int(num1) * int(num2) == 0):
            return num1 / num2
        else:
            return 'please enter the numbers'
    except ZeroDivisionError as err:
        return err
