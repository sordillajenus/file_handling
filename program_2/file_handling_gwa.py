class StudentGWAAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.top_student = " "
        self.top_gwa = float("inf")

    def create_file(self):
        file = open(self.filename, "w")
        file.close()

    def find_top_student(self):
        with open(self.filename, "r") as file:
            for line in file:
                if "-" in line:
                    new_line = line.split("-")
                    name = new_line[0].strip()
                    gwa = float(new_line[1].strip())

                    if gwa < self.top_gwa:
                        self.top_student = name
                        self.top_gwa = gwa

    def display_result(self):
        print(f"The student with the highest GWA is {self.top_student} with the general weighted average of {self.top_gwa}")


