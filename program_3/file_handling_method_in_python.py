# file = open("mylife.txt", "w")
# file.close()

with open("mylife.txt", "a") as file:
    while True:
        content = input("write something about your day: ")
        file.write(content + "\n")
        break
            

