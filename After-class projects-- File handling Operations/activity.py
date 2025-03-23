file_name = "students.txt"
with open(file_name, "w") as file:
    file.write("Roy, Math\n")
    file.write("Emma, Science\n")
    file.write("Liam, English\n")

with open(file_name, "r") as file:
    content = file.read()
    print("Full Content:")
    print(content)

with open(file_name, "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

with open(file_name, "r") as file:
    lines = file.readlines()
    print("Readlines Output:")
    print(lines)

with open(file_name, "w") as file:
    file.write("New Student, History\n")
    print("File overwritten successfully.")

with open(file_name, "a") as file:
    file.write("Sophia, Biology\n")
    print("New student added to the file.")

with open(file_name, "r") as file:
    print("Updated File Content:")
    print(file.read())
