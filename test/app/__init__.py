import re

def check_pwd(pwd):
    bb = re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$", pwd, flags=0)
    return bb