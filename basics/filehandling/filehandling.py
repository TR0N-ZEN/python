# f = open("old.txt")
# text = f.read()
# f.close()
# print(text)

"""
tries to execute the indented block of code
if that does not work due to an error
the following except blocks are executed if
the error matches the type of error occured in the try block
"""
try:
    # open(filename , mode) open(<string>, <string>) <=> open("(x of A*)", ("[r|a|w|x] [e|b|t]")) with A being the alphabet, so A* the amount of all words over that alphabet
    with open("old.txt", "r") as a:
        letter1 = a.read()
        a.close()
except FileNotFoundError:
    letter1 = None
    print("failure: old.txt not recognized")

try:
    with open("new.txt", "w") as b:
        b.write(letter1)
except:
    with open("new.txt", "x") as b:
        b.write(letter1)
print("everything should have went well")

