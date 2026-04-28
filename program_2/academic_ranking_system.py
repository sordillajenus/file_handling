import numpy as np
import statistics

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
            open(self.academic_report, "a") as file_2:

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
        with open(self.file_name, "r") as file_1, \
            open(self.academic_report, "a") as file_2:

            excellent = []
            good = []
            passed = []
            failed = []

            for line in file_1:
                lines = line.split("-")
                names = lines[0].strip()
                avg = float(lines[1].strip())

                if avg <= 1.50:
                    excellent.append((names, avg))
                elif 1.51 <=  avg <= 2.50:
                    good.append((names, avg))
                elif 2.51 <= avg <= 3.00:
                    passed.append((names, avg))
                else:
                    failed.append((names, avg))
        file_2.write("\nACADEMIC INSIGHT\n")
        number_excellent = len(excellent)
        number_good = len(good)
        number_passed = len(passed)
        number_failed = len(failed)

        if number_excellent > number_good and number_excellent > number_passed and number_excellent > number_failed:
            file_2.write(
            """\nThe majority of students are classified under the Excellent range, indicating a very strong overall academic performance. 
            This suggests high mastery of the subject matter and consistent study habits across most of the class.\n""")
        elif number_good > number_excellent and number_good > number_passed and number_good > number_failed:            file_2.write(
                """\nThe majority of students fall within the Good range, indicating a generally strong but not exceptional performance level.
                  This suggests that most students are performing well, with room for improvement toward excellence\n""")
        elif number_passed > number_excellent and number_passed > number_good and number_passed > number_failed:            file_2.write(
                """\nThe majority of students are in the Passed range, indicating an average overall performance. 
                While most students meet the minimum requirements, there is limited academic excellence observed.\n""")
        elif number_failed > number_excellent and number_failed > number_good and number_failed > number_passed:            file_2.write(
                """\nThe majority of students fall under the Failed category, indicating serious academic difficulties within the class. 
                This suggests a need for intervention, remediation, and stronger academic support\n""")
        else:
            file_2.write(
                """\nThe students are widely distributed across all performance categories (Excellent, Good, Passed, and Failed) with no clear majority or dominant range. 
                This indicates a highly heterogeneous class performance, where students vary significantly in academic achievement\n""")

    def gwa_statistics_engine(self):
        with open(self.file_name, "r") as file_1, \
            open(self.academic_report, "a") as file_2:

            average = []
            for line in file_1:
                lines = line.split("-")
                avg = float(lines[1].strip())
                average.append(avg)
            
            mean = sum(average)/len(average)
            median = np.median(average)
            gwa_gap = max(average) - min(average)
            standard_deviation = statistics.stdev(average)

            file_2.write("\n📊 GWA Statistics\n\n")
            file_2.write(f"(Mean) Average GWA of the Class: {mean}\n")
            file_2.write(
                """\nThe average GWA represents the overall academic performance of the class. It shows the general standing of students when all grades are combined. 
                A lower average indicates stronger performance across the group, while a higher average suggests that most students are performing at a moderate or lower level.\n\n""")
            file_2.write(f"Median GWA: {median}\n")
            file_2.write(
                """\nThe median GWA reflects the middle point of all student grades when arranged from lowest to highest. 
                It shows the typical performance level of the class without being affected by extremely high or low values. If the median is close to the average, it suggests a balanced distribution of grades. 
                If there is a large difference between them, it may indicate uneven performance among students.\n\n""")
            file_2.write(f"Highest vs Lowest GWA gap: {gwa_gap}\n")
            file_2.write(
                """\nThis measures the difference between the highest-performing student and the lowest-performing student. A small gap suggests that the class performance is relatively consistent. 
                A large gap, on the other hand, indicates a wide difference in academic achievement, showing that some students are significantly ahead while others are struggling.\n\n""")
            file_2.write(f"Standard Deviation:{standard_deviation}")
            file_2.write(
                """\nStandard deviation shows how spread out the grades are from the average. A low value means that most students have similar GWA scores, indicating consistency in performance. 
                A high value means that grades vary widely, showing inconsistency in understanding and academic performance across the class.\n\n""")
            file_2.write("CONCLUSION\n\n")
            file_2.write(
                """\nThe difference between the upper and lower GWA for each group indicates how far apart from one another stand the best students versus those who performed weakest, while latter will tell you how sharply centralized or dispersed were grades overall. 
                If both are low then the class is very homogeneous and we have students performing at similar levels. Then both are high: this indicates a clear separation between strong and weak performers. A wide delta with a low standard deviation usually means that most students are very close performance-wise but some outliers make the difference, 
                while a narrow delta with high (or higher) standard deviation suggests there is still variation across students though the overall gap might be narrower. In a nutshell, these are steps to give us an understanding of the overall performance and whether we have even class or not; 
                that is also helpful in identifying which group need attention.\n""")
            

            




                    


                





    