import csv

def readFromFile():
    company = []
    numEmployees = []
    ceoSalary = []
    with open("2024/companies.csv", "r") as file:
        print(file)
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(row[1])
            ceoSalary.append(row[2])

    return company, numEmployees, ceoSalary


def findCeoDiffrence(company, ceoSalary):
    maxIndex = 0
    for salaryIndex in range(len(ceoSalary)):
       if ceoSalary[salaryIndex] > ceoSalary[maxIndex]:
          maxIndex = salaryIndex
    pass

print(maxIndex)


chosenCompany = input("While company?: ")
for index in range(len(company)):

findCeoDiffrence()

# def findHighestEmployees(numEmployees):
#     pass

# #main
company, numEmployees, ceoSalary = readFromFile()
FindCeoDiffrence(company, ceoSalary)
# findHighestEmployees(numEmployees)
readFromFile()