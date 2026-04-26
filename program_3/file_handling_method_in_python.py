# file = open("mylife.txt", "w")
# file.close()

with open("mylife.txt", "a") as file:
    while True:
        content = input("Write something about your day: ")
        file.write(content + "\n")
        
        question = input("Are there more lines? yes/no: ")

        if question == "no":
            break
            

