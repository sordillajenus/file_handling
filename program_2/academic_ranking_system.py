class AcademicInsightAnalysis:
    def __init__ (self, file_name, academic_report):
        self.file_name = file_name
        self.academic_report = academic_report

    def ranking(self):
        with open(self.file_name, "r") as file_1, \
            open(self.academic_report, "w") as file_2:

            students_ranking = {

            }
            for line in file_1:
                lines = line.split("-")
                names = lines[0].strip()
                average = float(lines[1].strip())
                students_ranking[names] = average

            rank = sorted(students_ranking.items(), key = lambda x: x[1])
            rank_number = 1
            file_2.write("Below is the ranking of students who have demonstrated exemplary academic performance. Their dedication, effort, and commitment have led them to achieve outstanding grades.\n\n")            
            for key, value in rank:
                file_2.write(f"Rank {rank_number}: {key} - {value}\n")
                rank_number += 1

    def performance_category(self):
        with open(self.file_name, "r") as file_1, \
            open(self.academic_report, "w") as file_2:

            execellent = []
            good = []
            passed = []
            failed = []

            for line in file_1:
                lines = line.split("-")
                names = lines[0].strip()
                avg = float(lines[1].strip())

                if avg <= 1.50:
                    execellent.append(names, avg)
                elif 1.51 >= avg <= 2.50:
                    good.append(names, avg)
                elif 2.51 >= avg <= 3.00:
                    passed.append(names, avg)
                else:
                    failed.append(names, avg)

            file_2.write("\n")
            file_2.write("PERFORMANCE CATEGORY\n\n")
            file_2.write("\n")
            file_2.write("🟢 Excellent (≤ 1.50)\n")
            for student, grade in execellent:
                file_2.write(f"{student} - {grade}\n")
            file_2.write("\n🟡 Good (1.51 - 2.50)\n")
            for student, grade in good:
                file_2.write(f"{student} - {grade}\n")
            file_2.write("🟠 Passed (2.51 - 3.00)\n")
            for student, grade in passed:
                file_2.write(f"{student} - {grade}\n")
            file_2.write("🔴 Failed (> 3.00)\n")
            for student, grade in failed:
                file_2.write(f"{student} - {grade}\n")
    
    def academic_insight_report(self):
        


                    


                





    