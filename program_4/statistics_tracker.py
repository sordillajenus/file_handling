class StatisticsTracker:
    def __init__ (self, even_file, odd_file, summary_report_file):
        self.even_file = even_file
        self.odd_file = odd_file
        self.summary_report_file = summary_report_file

        def generate_summary(self):
            even_numbers = []
            odd_numbers = []

        
            with open(self.even_file, "r") as file_1:
                for line in file_1:
                    line = line.strip()
                    if line:
                        even_numbers.append(int(line))

            with open(self.odd_file, "r") as file_2:
                for line in file_2:
                    line = line.strip()
                    if line:
                        odd_numbers.append(int(line))

                    



