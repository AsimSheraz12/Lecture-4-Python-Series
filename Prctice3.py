student = {}

key1 = input("Enter the name of first subject: ")
value1 = int(input("Enter the marks of first subject: "))
key2 = input("Enter the name of second subject: ")
value2 = int(input("Enter the marks of second subject: "))
key3 = input("Enter the name of third subject: ")
value3 = int(input("Enter the marks of third subject: "))

student[key1] = value1
student[key2] = value2
student[key3] = value3

print(student)

student2 = student.copy()
