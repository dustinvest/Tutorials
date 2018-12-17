

# R = Read
# W = Write
# R+ = Read and Write
# A = Append

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())
employee_file.close()

