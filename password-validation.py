#  In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. 
# Create a Python script to check the strength of the password. 

import re 
# In Python, re is the regular expression module. It stands for “regular expressions” and is used to 
# search, match, and manipulate text using patterns.
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%]).+$"
def enterPass():
    password = input("Enter your password: ")
    return password

def check_password_strength(x):
        if re.match(pattern,x) and len(x) >= 8:
            print("Your password is Strong Enough and matching all the Criteria.")
            return True
        else:
            print(f"""Your Entered Password: "{x}" is not strong enough
                Please Re-enter Strong password and it should have following criteria:
                    Minimum length: The password should be at least 8 characters long.
                    Contains both uppercase and lowercase letters.
                    Contains at least one digit (0-9).
                    Contains at least one special character (e.g., !, @, #, $, %).""")
            check_password_strength(enterPass())
             
check_password_strength(enterPass())
    