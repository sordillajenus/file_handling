class IntegersEvenOdd:
    def __init__ (self, integer_file, even_file, odd_file):
        self.integer_file = integer_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process(self):
        with open(self.integer_file, "r") as file_1, \
            open(self.even_file, "w") as file_2, \
            open(self.odd_file, "w") as file_3:
    
            for line in file_1:
                line = line.strip()
                if not line:
                    continue

                num = int(line)

                if num % 2 == 0:
                    file_2.write(str(num ** 2) + "\n")
                else:
                    file_3.write(str(num ** 3) + "\n")

method = IntegersEvenOdd(
    "integers_1.txt",
    "double.txt",
    "triple.txt"
)

method.process()

        
