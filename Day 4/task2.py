
text = str(input("Enter your text : "))
def count_characters(text):
    return text[::-1]
    
print(count_characters(text))

# loopong system
text = str(input("Enter your text : "))
rev_text =""
for char in text:
    rev_text = char +rev_text
print(rev_text)