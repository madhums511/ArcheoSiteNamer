from itertools import combinations


def findabbrs(str_, max_number=20):
    clean_str = []
    disp = []

    # Remove non alpha numeric
    for i in str_[1:]:
        if i.isalnum():
            clean_str.append(i.upper())

    # Make a unique list of atmost max_number combinations of 2 chars
    for i in list(set(combinations(clean_str, 2)))[:max_number]:
        temp = list(i)
        # Add first character
        temp.insert(0, str_[0].upper())
        disp.append("".join(temp))
    return disp
