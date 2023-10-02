
word=0
with open("c:\\sqlite3\\python.txt","r") as file:
    for l in file:
        words=l.split()
        word+=len(words)
with open("c:\\sqlite3\\python.txt","r") as file:
    lines=file.readlines()
totallines=len(lines)
print("Total number of lines:",totallines)
print("Total number of words:",word)
