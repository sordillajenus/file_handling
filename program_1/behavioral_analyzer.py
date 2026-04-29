class BehavioralAnalyzer:
    def __init__ (self, number_file, even_file, odd_file, analysis_file):
        self.number_file = number_file
        self.even_file = even_file
        self.odd_file = odd_file
        self.analysis_file = analysis_file

    def behavior(self):
        numbers = []

        with open(self.number_file, "r") as file_1, \
             open(self.even_file, "r") as file_2, \
             open(self.odd_file, "r") as file_3, \
             open(self.analysis_file, "w") as file_4:
             
            total_counter = 0
            for line in file_1:
                line = line.strip()
                if line == "":
                    continue
                try:
                    num = int(line)
                    numbers.append(num)
                    total_counter += 1
                except ValueError:
                    continue

            even_counter = 0
            for line_2 in file_2:
                line_2 = line_2.strip()
                if line_2 == "":
                    continue
                even_counter += 1   

            odd_counter = 0
            for line_3 in file_3:
                line_3 = line_3.strip()
                if line_3 == "":
                    continue
                odd_counter += 1

            file_4.write("BEHAVIORAL ANALYSIS" + "\n")
            file_4.write("\n")
            file_4.write("Dataset Summary" + "\n")
            file_4.write("\n")
            file_4.write("The dataset below contains the collection of numerical values extracted from the input file. After cleaning and validation, all valid integers were analyzed to determine patterns, distribution, and behavioral characteristics. " + "\n")
            file_4.write("\n")
            file_4.write("General Statistics" + "\n")
            file_4.write(f"Total Numbers: {total_counter}" + "\n")
            file_4.write(f"Valid Entries: {total_counter}" + "\n")
            file_4.write("\n")
            file_4.write("\n")

            even_percentage = (even_counter / total_counter) * 100
            odd_percentage = (odd_counter / total_counter) * 100
            file_4.write("Parity Distribution (Even vs Odd)" + "\n")
            file_4.write("\n")
            file_4.write(f"Even Numbers: {even_counter} ({even_percentage}%)" + "\n")
            file_4.write(f"Odd Numbers: {odd_counter} ({odd_percentage}%)" + "\n")
            file_4.write("\n")
            file_4.write("INTERPRETATION:" + "\n")
            file_4.write("\n")

            if even_counter > odd_counter:
                file_4.write("The dataset is dominated by even numbers, indicating a strong bias toward values divisible by 2. This suggests a structured or patterned input rather than random distribution. " + "\n")
            elif odd_counter > even_counter:
                file_4.write("The dataset is dominated by odd numbers, indicating a strong bias toward values not divisible by 2. This suggests a distinct numerical pattern, potentially reflecting intentional selection or a non-random distribution of values." + "\n")
            else:
                file_4.write("The dataset shows a balanced distribution of even and odd numbers, indicating no dominance of either group. This suggests a more uniform and potentially random distribution, with no clear bias toward values divisible or not divisible by 2." + '\n')

            if total_counter > 0:
                minimum = min(numbers)
                maximum = max(numbers)
                average = sum(numbers) / total_counter  
            file_4.write("\n")
            file_4.write("Value Characteristics" + "\n")
            file_4.write("\n")
            file_4.write(f"The minimum value is: {minimum}\n")
            file_4.write(f"The maximum value is: {maximum}\n")
            file_4.write(f"The average is: {average}\n")

            if average < 30:
                file_4.write("The dataset is composed primarily of small values, indicating concentration in the lower range.\n")
            elif average <= 70:
                file_4.write("The dataset shows a moderate distribution of values, suggesting a balanced spread.\n")
            else:
                file_4.write("The dataset is dominated by large values, indicating a shift toward higher magnitudes.\n")

            file_4.write("\nFinal Conclusion\n\n")

            if average < 30:
                file_4.write("Overall, the dataset is concentrated on smaller values with limited magnitude, suggesting controlled or constrained inputs.\n")
            elif average <= 70:
                file_4.write("Overall, the dataset demonstrates a balanced and stable distribution of values, indicating consistency and moderate variability.\n")
            else:
                file_4.write("Overall, the dataset exhibits a tendency toward larger values, suggesting emphasis on higher numerical ranges.\n")               

                

