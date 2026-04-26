# file = open("students_with_their_gwa.txt", "w")
# file.close()

top_student = " "
top_gwa = float("inf")

with open("students_with_their_gwa.txt", "r") as file:
    for line in file:
       if "-" in line:
        new_line = line.split("-")
        name = new_line[0].strip()
        gwa = float(new_line[1].strip())
        
        if gwa < top_gwa:
           top_student = name
           top_gwa = gwa

print(f"The student with the highest GWA is {top_student} with the general weighted average of {top_gwa}")

        
           

        




