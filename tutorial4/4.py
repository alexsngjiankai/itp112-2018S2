from entities import *

def is_valid_nric(s):
   valid = False
   if len(s)==9:
       if s[0].upper() == 'S' or s[0].upper() == 'T':
           if s[-1].isalpha() :
               if s[1:-1].isdigit():
                   valid = True
   return valid


def is_valid_gpa(gpa):
   valid = False
   if 0<=gpa<=4:
       valid = True
   return valid


studentList = []
employeeList = []
while True:
   while True:
       nric = input('Enter NRIC: ')
       nric_valid = is_valid_nric(nric)
       if nric_valid == False:
           print("Invalid NRIC!")
       else:
           break

   name = input('Enter Name: ')
   type = input('Student or Employee? (S or E): ')
   if type.lower() == 'e':

       salary = float(input('Enter Salary: $'))

       while salary <=0:
           print("Salary must be greater than $0")
           salary = float(input('Enter Salary: $'))


       e2 = Employee(nric, name, salary)
       employeeList.append(e2)
   else:
       gpa_valid = False
       while gpa_valid == False:
           gpa = float(input('Enter GPA:'))
           gpa_valid = is_valid_gpa(gpa)
           if gpa_valid == False:
               print("GPA is 0 to 4")

       s2 = Student(nric, name, gpa)
       studentList.append(s2)

   con = input('Do you want to continue to enter another Student or Employee? (Y or N): ')

   if con.lower() == 'n':
       break

print("======== Student ==========")
for i in studentList:
   print(i)

print("======== Employee ==========")
for j in employeeList:
   print(j)
