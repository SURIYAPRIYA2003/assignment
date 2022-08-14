from datetime import date
class company:

    def __init__(self,name,gender,dob,city,salary=100000):
        self.name=name
        self.gender=gender
        self.dob=dob
        self.city=city
        self.salary=salary

    def details(self):
        addr=f"Name : {self.name}\nGender : {self.gender}\nDOB : {self.dob}\ncity : {self.city}\nSalary : {self.salary}"
        return addr

    def year(self):
        current_year=date.today().year
        exp=current_year - self.dob
        return exp


stu1=company("Suriya","Female",2003,"Chennai")

print(stu1.details())
print(stu1.year())
