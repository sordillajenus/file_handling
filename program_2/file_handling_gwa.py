class StudentGWAAnalyzer:
    def __init__(self, filename, output_file):
        self.filename = filename
        self.output_file = output_file
        self.top_student = " "
        self.top_gwa = float("inf")

    def analyze(self):
        with open(self.filename, "r") as file:
            for line in file:
                if "-" in line:
                    new_line = line.split("-")
                    name = new_line[0].strip()
                    gwa = float(new_line[1].strip())

                    if gwa < self.top_gwa:
                        self.top_student = name
                        self.top_gwa = gwa

    def save_result(self):
        with open(self.output_file, "w") as file:
            file.write("STUDENT GWA ANALYSIS\n\n")
            file.write(f"Top Student: {self.top_student}\n")
            file.write(f"Highest Performance (Lowest GWA): {self.top_gwa}\n")

    def display(self):
        print(f"The student with the highest GWA is {self.top_student} with a GWA of {self.top_gwa}")



analyzer = StudentGWAAnalyzer(
    "students_with_their_gwa.txt",
    "gwa_analysis_report.txt"
)

analyzer.analyze()
analyzer.save_result()
analyzer.display()