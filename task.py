with open("templates.txt", "r", encoding="utf-8") as file:
    data = file.read().split("\n")
for i in data:
    if "\\n" in i:
        print(i.replace("\\n", "\n"))