def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))


########################################################################

def is_leap_year(year):
    if year % 4 == 0:
        if  year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Best Practice
def is_leap_year2(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(1989))  # Output: False
print(is_leap_year(2000))  # Output: True
print(is_leap_year(1900))  # Output: False
print(is_leap_year2(1989))  # Output: False
print(is_leap_year2(2000))  # Output: True
print(is_leap_year2(1900))  # Output: False


