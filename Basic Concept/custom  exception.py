class Salaryerror(Exception):
      pass
def check_salary(salary):
    if salary < 0:
        raise Salaryerror("Salary cannot be negative")
    else:
        bonus=0.1*salary
        return salary+bonus

salary=int(input("Enter your salary: "))
final=check_salary(salary)
print(final)
