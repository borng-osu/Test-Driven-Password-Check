import string

def check_pwd(pwd):
    # Checks if pwd is a string
    if type(pwd) is str:
        # Checks if pwd length is valid
        if 7 < len(pwd) < 20:
            return True
    return False
