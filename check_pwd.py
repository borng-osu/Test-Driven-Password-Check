import string


def check_pwd(pwd):
    """Function that takes pwd string as parameter,
    checks whether it is a valid password,
    and returns boolean upon verification."""
    # Checks if pwd is a string
    if type(pwd) is str:
        # Checks if pwd length is valid
        if 7 < len(pwd) < 20:
            # Initializes valid symbols and symbol check
            symbols = "~`!@#$%^&*()_+-="
            sym_check = False
            # Initializes lowercase, digit, and uppercase checks
            low_check = False
            up_check = False
            digit_check = False
            # Iterates through pwd to check if valid characters present
            for i in range(len(pwd)):
                if sym_check and low_check and up_check:
                    break
                elif pwd[i] in symbols:
                    sym_check = True
                elif pwd[i] in string.ascii_lowercase:
                    low_check = True
                elif pwd[i] in string.ascii_uppercase:
                    up_check = True
                elif pwd[i] in string.digits:
                    digit_check = True
            # Returns False if checks not passed
            if not sym_check or not low_check \
                    or not up_check or not digit_check:
                return False
            return True
    return False
