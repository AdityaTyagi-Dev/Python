import csv

with open("students.csv", "w", newline = "") as file:
    writer = csv.writer(file) # creating a writer object

    writer.writerow(["Name", "Age", "City"]) # writing one row at a time
    writer.writerow(["Rahul", 17, "Jaipur"])
    writer.writerow(["Anita", 18, "Delhi"])

    writer.writerows([["Mohit", 16, "Mumbai"], ["Suman", 17, "Kolkata"]]) # writing multiple rows at a time

with open("students.csv", "r") as file:
    reader = csv.reader(file) # creating a reader object

    for row in reader:
        print(row) # reading all the data

with open("Students2.csv", "w", newline = "") as file:  # reading and writing data as a dictionary
    fields = ["Name", "Age", "City"]

    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()
    writer.writerow({
        "Name" : "Rahul",
        "Age" : 17,
        "City" : "Jaipur"
    })

with open("Students2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)