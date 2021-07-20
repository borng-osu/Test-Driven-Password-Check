import string

def check_pwd(pwd):
    # Checks if pwd is a string
    if type(pwd) is str:
        # Checks if pwd length is valid
        if 7 < len(pwd) < 20:
            # Initializes valid symbols and symbol count
            symbols = "~`!@#$%^&*()_+-="
            sym_check = 0
            # Iterates through pwd to check if valid characters present
            for i in range(len(pwd)):
                if pwd[i] in symbols:
                    sym_check += 1
            # Returns False if no symbols are in pwd
            if sym_check == 0:
                return False
            return True
    return False
