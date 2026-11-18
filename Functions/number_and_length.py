def check_number_and_length(password_string: str) -> None:
    """
    Checks if the password contains at least one number
    and has a minimum length of 14 characters.
    """

    # Initialize variables to check the password requirements
    has_number = False
    has_enough_length = False

    # Iterate through the password to find at least one digit
    for character in password_string:
        if character.isdigit():
            has_number = True

    # Check if the password meets the minimum length requirement
    if len(password_string) >= 14:
        has_enough_length = True

    return has_number and has_enough_length

