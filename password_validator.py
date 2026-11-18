from Functions.uppercase import check_upper
from Functions.lowercase import check_lower
from Functions.number_and_length import check_number_and_length
from Functions.symbol import check_valid_symbol
from Functions.cracking_time import time_needed
from termcolor import colored

Recommendations = ""
password = str(input(colored("[+] Enter your password: ", "blue")))
if not check_number_and_length(password):
    Recommendations += "The password must contain at least one number and be at least 14 characters long.\n"
if not check_lower(password):
    Recommendations += "The password must contain at least one lowercase letter.\n"
if not check_upper(password):
    Recommendations += "The password must contain at least one uppercase letter.\n"
if not check_valid_symbol(password):
    Recommendations += "The password must contain at least one valid symbol and no spaces or disallowed characters.\n"

if Recommendations == "":
    print(colored("[+] Your password is strong.", "green"))
    print(colored("[+] Your password would be cracked in: " + str(time_needed(password)) + " seconds.", "green"))
else:
    print(colored("[!] Your password has the following issues:", "red"))
    print(Recommendations)

