def is_the_same(message1, message2):
    if len(message1) == len(message2) and sorted(message1) == sorted(message2):
        return "Your words are the same"
    elif len(message1) != len(message2) or sorted(message1) != sorted(message2):
        return "Your words are not the same"


message1 = input("Please enter your word: ")
message2 = input("Please enter your second word: ")
message1 = message1.strip()
message1 = message1.lower()
message2 = message2.strip()
message2 = message2.lower()
result = is_the_same(message1, message2)
print(result)
