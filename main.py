# def fancy_hello_world():
#     fancy_string = """
#     ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
#     ───█▒▒░░░░░░░░░▒▒█───
#     ────█░░█░░░░░█░░█────
#     ─▄▄──█░░░▀█▀░░░█──▄▄─
#     █░░█─▀▄░░░░░░░▄▀─█░░█
#     """
#     return fancy_string
#
#
# print(fancy_hello_world())


# def absolute_value(x):
#     if x < 0:
#         return -x
#     elif x >= 0:
#         return x
#
#
# print(absolute_value(0))

# x = input("Input 1st num to compare: ")
# y = input("Input 2nd num to compare: ")


# def compare():
#     if x > y:
#         return 1
#     elif x ==y:
#         return 0
#     elif x < y:
#         return -1
#
#
# print(compare())


# myVariable = int(input("Input something: "))
#
#
# def test_is_valid():
#     if isinstance(myVariable, int) and myVariable in range(1,4):
#         return True
#     else:
#         return False
#
#
# print(test_is_valid())

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find('computer', 'p', 1))
