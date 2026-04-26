file = open("numbers.txt", "w")
file.close()

with open("numbers.txt", "r") as file_1, \
     open("even.txt", "w") as file_2, \
     open("odd.txt", "w") as file_3:
    
    for line in file_1:
        line = line.strip()
        if line == " ":
            continue

        num = int(line)

        if num % 2 == 0:
            file_2.write(str(num) + "\n")
        else:
            file_3.write(str(num) + "\n")