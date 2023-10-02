uniquewords=0
with open("c:\\sqlite3\\python.txt","r") as file:
        l=file.read()
        word=set(l.split())
print("total unique words:",len(word))
print("Unqiue words are:",word)
