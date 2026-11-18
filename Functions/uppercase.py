def check_upper(password):
    """
    Checks whether the password contains an uppercase letter.
    
    Arguments:
        password: The password entered by the user.

    Returns:
        True if the password contains an uppercase letter.
        False if the password does not contain an uppercase letter.
    """

    # Check each letter in the password
    for letter in password:
        # Check if the current letter is between A and Z
        if letter >= "A" and letter <= "Z":
            # Return True because an uppercase letter was found
            return True
        
    # Return False because the password has no uppercase letters
    return False

