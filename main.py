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
print(letter1)

#wirte to txt files
b = [1,2,3,4]
with open("new.txt" ,"x") as b:
    b.write(letter1)