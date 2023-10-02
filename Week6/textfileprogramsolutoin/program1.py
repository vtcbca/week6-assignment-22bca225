# Read Python.txt file and Print it in Reverse.

file="C:\\sqlite3\\python.txt"
with open (file,"r") as file:
    r=file.read()
reverse=r[::-1]
print(reverse)
