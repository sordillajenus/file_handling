class IntegersEvenOdd:
    def __init__ (self, integer_file, even_file, odd_file):
        self.integer_file = integer_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process(self):
        with open("integers_1.txt", "r") as file_1, \
            open("double.txt", "w") as file_2, \
            open("triple.txt", "w") as file_3:
    
            for line in file_1:
                line = line.strip()
                if line == " ":
                    continue

        num = int(line)

        squared = num ** 2
        file_2.write(str(squared) + "\n")
        cubed = num ** 3
        file_3.write(str(cubed) + "\n")
        
