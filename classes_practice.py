class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)


emp_1.name = 'Abu Sakib'
emp_1.email = 'mabusakib@gmail.com'
emp_1.sal = 30000

emp_2.name = 'Abu Salek'
emp_2.email = 'mabusalek@gmail.com'
emp_2.sal = 60000

print("Employee no. 1")
print(emp_1.name)
print(emp_1.email)
print(emp_1.sal)

print("\n")

print("Employee no. 2")
print(emp_2.name)
print(emp_2.email)
print(emp_2.sal)
