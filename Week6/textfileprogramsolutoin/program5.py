file="C:\\sqlite3\\python.txt"
f="c:\\sqlite3\\python_upper.txt"
with open(file,"r")as file:
    data=file.read()
upper=data.upper()
with open(f,"w") as txt:
    text=txt.write(upper)

