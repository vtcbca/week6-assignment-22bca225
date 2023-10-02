with open("c:\\sqlite3\\python.txt","r") as file:
        l=file.read()
        word=l.split()
        largest=small=word[0]
        for i in range(0,len(word)):
            if (len(largest)<len(word[i])):
                largest=word[i]
            elif(len(small)>len(word[i])):
                  small=word[i]
print("largest word:",largest)
print("smallest word:",small)
