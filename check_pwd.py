import string

def check_pwd(pwd):
    # Checks if pwd is a string
    if type(pwd) is str:
        # Checks if pwd length is valid
        if 7 < len(pwd) < 20:
            # Initializes valid symbols and symbol check
            symbols = "~`!@#$%^&*()_+-="
            sym_check = False
            # Initializes lowercase letter count
            low_check = False
            # Iterates through pwd to check if valid characters present
            for i in range(len(pwd)):
                if sym_check and low_check:
                    break
                elif pwd[i] in symbols:
                    sym_check += True
                elif pwd[i] in string.ascii_lowercase:
                    low_check += True
            # Returns False if no symbols in pwd
            if not sym_check:
                return False
            # Returns False if no lowercase letters in pwd
            if not low_check:
                return False
            return True
    return False
