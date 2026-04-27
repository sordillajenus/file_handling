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


                





    