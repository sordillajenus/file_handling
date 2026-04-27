class BehavioralAnalyzer:
    def __init__ (self, number_file, even_file, odd_file, analysis_file):
        self.number_file = number_file
        self.even_file = even_file
        self.odd_file = odd_file
        self.analysis_file = analysis_file

    def behavior(self):
        with open(self.number_file, "r") as file_1, \
             open(self.even_file, "r") as file_2, \
             open(self.odd_file, "r") as file_3, \
             open(self.analysis_file, "w") as file_4:
            
            total_counter = 0
            for line in file_1:
                line = line.strip()
                if line == "":
                    continue
                num = len((line))
                total_counter += num
            even_counter = 0
            for line_2 in file_2:
                line_2 = line_2.strip()
                if line_2 == "":
                    continue
                num_2 = len(line_2)
                even_counter += num_2
            odd_counter = 0
            for line_3 in file_3:
                line_3 = line_3.strip()
                if line_3 == "":
                    continue
                num_3 = len(line_3)
                odd_counter += num_3

                file_4.write("BEHAVIORAL ANALYSIS" + "\n")
                file_4.write("\n")
                file_4.write("Dataset Summary" + "\n")
                file_4.write("\n")
                file_4.write("The dataset below contains the collection of numerical values extracted from the input file. After cleaning and validation, all valid integers were analyzed to determine patterns, distribution, and behavioral characteristics. " + "\n")
                file_4.write("\n")
                file_4.write("General Statistics" + "\n")
                file_4.write(f"Total Numbers: {total_counter}" + "\n")
                file_4.write(f"Valid Entries: {total_counter}" + "\n")
                
                if even_counter > odd_counter:
                    file_4.write("The text file shows that the content is even-dominated. This means that ")

                

                

