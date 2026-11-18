def time_needed(string):
    """
    Calculates the time needed to crack a password based on its length and character set.
    """

    # Define the character sets
    lowercase_letters = 26
    uppercase_letters = 26
    numbers = 10
    symbols = 27  # 5 are excluded, so we have 32 - 5 = 27 valid symbols

    # Calculate the total number of possible characters
    total_characters = lowercase_letters + uppercase_letters + numbers + symbols

    # Calculate the total number of combinations for the given password length
    total_combinations = total_characters ** len(string)

    # Assume a cracking speed of 1 billion guesses per second (1e9)
    cracking_speed = 1e9

    # Calculate the time needed to crack the password in seconds
    time_in_seconds = total_combinations / cracking_speed

    # Convert seconds into a readable unit
    years = time_in_seconds / 31536000  # 60 * 60 * 24 * 365
    if time_in_seconds < 1:
        return "Instantly (< 1 second)"
    elif time_in_seconds < 60:
        return f"{time_in_seconds:.2f} seconds"
    elif time_in_seconds < 3600:
        return f"{time_in_seconds / 60:.2f} minutes"
    elif time_in_seconds < 86400:
        return f"{time_in_seconds / 3600:.2f} hours"
    elif time_in_seconds < 31536000:
        return f"{time_in_seconds / 86400:.2f} days"
    elif years < 1_000:
        return f"{years:.2f} years"
    elif years < 1_000_000:
        return f"{years / 1_000:.2f} thousand years"
    elif years < 1_000_000_000:
        return f"{years / 1_000_000:.2f} million years"
    elif years < 1_000_000_000_000:
        return f"{years / 1_000_000_000:.2f} billion years"
    else:
        return f"{years / 1_000_000_000_000:.2f} trillion years"

