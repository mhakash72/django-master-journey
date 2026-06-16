text = input("Enter our text : ")

def is_palindrome(text):
    rev_text = text[::-1]
    return True if text == rev_text else False
    
print(is_palindrome(text))