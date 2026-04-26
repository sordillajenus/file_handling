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

            even_counter = len(even_numbers)
            odd_counter = len(odd_numbers)

            even_sum = sum(even_numbers)
            odd_sum = sum(odd_numbers)

            highest_even = max(even_numbers)
            highest_odd = max(even_numbers)

            with open(self.summary_file, "w") as file_3:
                file_3.write("STATISTICAL SUMMARY:" + "\n")
                file_3.write("\n")
                file_3.write("EVEN SECTION:" "\n")
                file_3.write(f"The number of even numbers are: {even_counter}" + "\n")
                file_3.write(f"The sum of even numbers are: {even_sum}" + "\n")
                file_3.write(f"The highest even number is: {highest_even}" + "\n")      
                file_3.write("\n")  
                file_3.write("ODD SECTION:" + "\n") 
                file_3.write(f"The number of odd numbers are: {odd_counter}")  
                file_3.write(f"The sum of odd numbers are: {odd_sum}") 
                file_3.write(f"The highest odd number is: {highest_odd}")    


            

        


                    



