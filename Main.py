def slicing(text):
    reversed_text = text[::-1]
    print(reversed_text)  # Output reverse string via slicing method.

def reverse_and_join(text):
    reversed_text = ''.join(reversed(text))
    print(reversed_text)  # Output reverse string via reverse() and join().

def loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    print(reversed_text)  # Output reverse string via for loop method.


text = input("Enter a string: ")
print("You entered:", text)
method = input("Enter a method: slicing, join, or loop:")
if method == "slicing":
    slicing(text)
if method == "join":
    reverse_and_join(text)
if method == "loop":
    loop(text)
else:
    print("Sorry, you got to enter one of the three. Good Bye!")

