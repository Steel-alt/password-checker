def check_valid_symbol(string: str) -> bool:
    """
    Checks if the password has at least one valid symbol and no spaces or disallowed characters.
    """

    found_symbol = False

    bad_characters = "\"'\\<>" # Quotes, backslash, and angle brackets are not usually allowed in passwords

    for character in string:
        # 1. Reject spaces or bad characters immediately
        if character.isspace() or character in bad_characters:
            return False

        # 2. Check for valid symbols
        if not character.isalnum():
            found_symbol = True

    return found_symbol

