class MyLifeWriter:
    def __init__ (self, filename):
        self.file_name = filename

    def initialize_file(self):
        with open(self.file_name, "w", encoding="utf-8")
            pass


file = open("mylife.txt", "w")
file.close()

with open("mylife.txt", "a") as file:
    while True:
        content = input("Write something about your day: ")
        file.write(content + "\n")
        
        question = input("Are there more lines? yes/no: ")
        if question not in ["yes", "no"]:
            print("Invalid input")

        if question == "no":
            break
        

