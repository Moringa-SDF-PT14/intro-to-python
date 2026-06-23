# access files (context manager)

# Open a file in read only mode
with open("names.txt", "r") as names_file:
    for line in names_file:
        print(line.strip())


# Open a file in write mode (overwrite)
with open("names.txt", "w") as names_file:
    names_file.write("Eddie\n")
    names_file.write("Deborah\n")

