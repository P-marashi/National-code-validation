import re


# validate national code in here
def is_valid_iran_code(input: str) -> bool:
    if not re.search(r'^\d{10}$', input): return False
    check = int(input[9])
    s = sum(int(input[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11


# test the code with this function
def test():
    number = input("enter national code: ")
    check = is_valid_iran_code(number)
    print(check)


test()
