from life_analytics import LifeAnalytics

class MyLifeWriter:
    def __init__ (self, filename):
        self.file_name = filename

    def write_entries(self):
        with open(self.file_name, "a", encoding="utf-8") as file:
         
         while True:
            content = input("Write something about your day: ")
            file.write(content + "\n")

            while True:
                    question = input("Are there more lines? yes/no: ").lower()

                    if question in ["yes", "no"]:
                        break
                    else:
                        print("Invalid input. Please type 'yes' or 'no'.")

            if question == "no":
                break

    def run(self):
        self.write_entries()

writer = MyLifeWriter("mylife.txt")
writer.run()

analyzer = LifeAnalytics("mylife.txt")
analyzer.run()


        
        

