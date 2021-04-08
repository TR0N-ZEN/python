#f = open("old.txt")
#text = f.read()
#f.close()
#print(text)

try:
    with open("old.txt","r",) as a: # open(filename, mode) <=> open(<string>, <string>) <=> open("(x of A*)", ("[r|a|w|x] [e|b|t]")) with A being the alphabet, so A* the amount of all words over that alphabet
        letter1 = a.read()
        a.close()
except FileNotFoundError: # on FileNotFoundError indeted codeblock will be executed
    letter1 = None
    print("failure: old.txt not recognized")

#tries to open file ("new.txt") in write mode ("W")
try:
    with open("new.txt" ,"w") as b:
        b.write(letter1)
#if trie failed due to an occuring error it triggers the next except command (e.g. here in the next line)
except:
    with open("new.txt" ,"x") as b:
        b.write(letter1)
print("everything should have went well")