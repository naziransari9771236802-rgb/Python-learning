text = "hello world"

# 1. upper()
print(text.upper())          # HELLO WORLD

# 2. lower()
print(text.lower())          # hello world

# 3. capitalize()
print(text.capitalize())     # Hello world

# 4. title()
print(text.title())          # Hello World

# 5. swapcase()
print(text.swapcase())       # HELLO WORLD

# 6. find()
print(text.find("o"))        # 4

# 7. index()
print(text.index("w"))      # 6

# 8. count()
print(text.count("l"))       # 3

# 9. startswith()
print(text.startswith("hello"))  # True

# 10. endswith()
print(text.endswith("world"))   # True

# 11. strip()
print("  hello  ".strip())   # hello

# 12. lstrip()
print("  hello".lstrip())    # hello, left side space remove

# 13. rstrip()
print("hello  ".rstrip())   # hello, right side space remove

# 14. replace()
print(text.replace("world", "Python"))  # hello Python

# 15. split()
print(text.split())          # ['hello', 'world']

# 16. rsplit()
print("a-b-c".rsplit("-", 1))  # ['a-b', 'c'], right side se split krna 

# 17. join()
print("-".join(["a", "b", "c"]))  # a-b-c

# 18. partition()
print("a-b-c".partition("-"))  # ('a', '-', 'b-c'), according to string exactly 3 parts me divide krna

# 19. isalpha
print("hello".isalpha())     # True, check only Alphabets or not

# 20. isdigit()
print("12345".isdigit())     # True, check only Digits check

# 21. isalnum()
print("abc123".isalnum())    # True, check alphabets + number check

# 22. isspace()
print("   ".isspace())       # True, check string whitespace or not

# 23. islower()
print("hello".islower())     # True, string all cased lowercase or not

# 24. isupper()
print("HELLO".isupper())     # True,  string all cased Uppercase or not

# 25. istitle()
print("Hello World".istitle())  # True, check krta h ki har word ka first letter uppercase h aur baki cased letters lowercase hain ya nhi

# 26. isascii()
print("Hello".isascii())     # True, Check karta hai ki String ke saare characters ASCII range (0–127) mein hain ya nahi.
# ASCII mein English letters, digits aur common symbols aate hain.

# 27. center()
print("Hi".center(10, "-"))  # ----Hi----, String ko given width ke andar center position par rakhta hai.

# 28. ljust()
print("Hi".ljust(10, "-"))   # Hi--------, String ko left side mein rakhta hai aur right side mein extra characters add karta hai.

# 29. rjust()
print("Hi".rjust(10, "-"))   # --------Hi, String ko right side mein rakhta hai aur left side mein extra characters add karta hai.

# 30. zfill()
print("25".zfill(5))         # 00025, String ke starting mein zeros add karta hai taaki given width complete ho jaye.

