def check_lower(password):
# Create a false variable
    have_lower = False
# We check the password letter by letter to detect a lower
    for letter in password:
#If lowercase, set to True
        if letter.islower():
            have_lower = True
#If no lower found
    if have_lower == False:
        return False
    return True

