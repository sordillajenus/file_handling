class MyLifeWriter:
    def __init__ (self, filename):
        self.file_name = filename

    def initialize_file(self):
        with open(self.file_name, "w", encoding="utf-8"):
            pass

    def write_entries(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
         
         while True:
            content = input("Write something about your day: ")
            file.write(content + "\n")

            while True:
        
        question = input("Are there more lines? yes/no: ")
        if question not in ["yes", "no"]:
            print("Invalid input")

        if question == "no":
            break
        

