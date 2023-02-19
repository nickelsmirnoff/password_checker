import re
str_input = "Passw9rd"

def pass_checker(string):
    if not (6 <= len(string) <= 12):
        return False
    symb_dict = {
                'az': 0, 'AZ': 0,
                '09': 0, 'sp': 0
                }
    # print(re.search(r"\d",string))
    if re.search(r"\d",string):
        symb_dict['09'] = 1
    # print(re.search(r"[a-z]", string))
    if re.search(r"[a-z]", string):
        symb_dict['az'] = 1
    # print(re.search(r"[A-Z]", string))
    if re.search(r"[A-Z]",string):
        symb_dict['AZ'] = 1
    # print(re.search(r"[.,:;!_*-+()/#¤%&@]",string))
    if re.search(r"[.,:;!_*-+()/#¤%&@]",string):
        symb_dict['sp'] = 1
    # print(symb_dict)
    arr = symb_dict.values()
    if min(arr) == 0:
        return False
    else:
        return True

print(pass_checker(str_input))