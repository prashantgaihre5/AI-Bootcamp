def is_palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    text = input("Enter a string or number to check if it's a palindrome: ")
    if is_palindrome(text):
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is not a palindrome.")
