# file = open("students_with_their_gwa.txt", "w")
# file.close()

with open("students_with_their_gwa.txt", "r") as file:
    for line in file:
        print(line)