# file = open("mylife.txt", "w")
# file.close()

with open("mylife.txt", "a") as file:
    while True:
        content = input("Write a line from your diary: ")
        file.append(content)

