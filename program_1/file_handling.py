class IntegerManipulation:
    def __init__ (self, number_file, even_file, odd_file):
        self.number_file = number_file
        self.even_file = even_file
        self.odd_file = odd_file

    with open(self.number_file, "r") as file_1, \
        open(self.even_file, "w") as file_2, \
        open(self.odd_file, "w") as file_3:
    
        for line in file_1:
            line = line.strip()
            if line == " ":
                continue

            num = int(line)

            if num % 2 == 0:
                file_2.write(str(num) + "\n")
            else:
                file_3.write(str(num) + "\n")