def missingCharacters(s):
    digits = set("0123456789")
    letters = set("abcdefghijklmnopqrstuvwxyz")

    present_digits = set(filter(str.isdigit, s))
    present_letters = set(filter(str.isalpha, s))

    missing_digits = sorted(digits - present_digits)
    missing_letters = sorted(letters - present_letters)

    return ''.join(missing_digits + missing_letters)


# Optional for local testing
if __name__ == '__main__':
    s = input("Enter the string: ")
    print("Missing characters:", missingCharacters(s))
