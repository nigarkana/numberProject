def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


def is_even(n):
    return not is_odd(n)


def odd_or_even(n):
    if is_odd(n):
        return "odd"
    else:
        return "even"


def is_digit(s):
    # check if s contains only one character
    if len(s) != 1:
        return False

    digits = "0123456789"
    for digit in digits:
        if digit == s:
            return True
    return False


def is_integer(str_num):
    if len(str_num) == 0:
        return False

    for num in str_num:
        if not is_digit(num):
            return False

    return True


def odd_or_even_str_to_int_conversion(str_num):
    # check if the string is an integer
    if is_integer(str_num):
        # if ture then convert the string into integer
        num = int(str_num)
        # then check if the converted value is odd or even
        return odd_or_even(num)
    # if not then raise an Exception ValueError with message "Invalid Number"
    else:
        raise ValueError("Invalid Number")


def odd_or_even_str_to_int_conversion_2(str_num):
    try:
        num = int(str_num)
        return odd_or_even(num)
    except:
        raise ValueError("Invalid Number")
