tree = "master"
version = "1.0"
author = "TR0N"
print("tree:" + tree)
print("version:" + version)
print("by" + author)
print("#################################################################################################################################################################################################################")

#f = open("old.txt")
#text = f.read()
#f.close()
#print(text)

try:
    with open("old.txt","r",) as a:
        letter1=a.read()
        a.close()
except FileNotFoundError:
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