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

                if even_counter > odd_counter:
                    file_4.write()

                

                

