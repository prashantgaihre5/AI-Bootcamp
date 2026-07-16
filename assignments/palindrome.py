text = input("Enter a string or number to check if it's a palindrome: ")
text_cleaned = str(text).lower().replace(" ", "")

if text_cleaned == text_cleaned[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
