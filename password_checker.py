import re
str_input = input("Input new password: ")

def pass_checker(string_checked):
    if not (6 <= len(string_checked) <= 12):
        return False
    symb_dict = {
                'az': 0, 'AZ': 0,
                '09': 0, 'sp': 0
                }

    if re.search(r"\d",string_checked):
        symb_dict['09'] = 1
    if re.search(r"[a-z]", string_checked):
        symb_dict['az'] = 1
    if re.search(r"[A-Z]",string_checked):
        symb_dict['AZ'] = 1
    if re.search(r"[^\d\w]",string_checked):
        symb_dict['sp'] = 1
    return min(symb_dict.values()) == 0


print(pass_checker(str_input))