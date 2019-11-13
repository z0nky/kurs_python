class Pracownik:

    company = "Kowalski is the best"

    def __init__(self, job, salary, name, surname, years, is_student):
        self.job = job
        self.salary = salary
        self.name = name
        self.surname = surname
        self.years = years
        self.is_student = is_student

    def raises(self):
        if self.job == "szef":
            self.salary *= 1.5
            # self.salary = self.salary * 1.5
            return self.salary
        elif self.job == "stażysta":
            self.salary = self.salary * 0.1
            return self.salary
        else:
            self.salary = self.salary * 0.2
            return self.salary

    def taxes(self):
        taxes = self.salary * 0.1
        return taxes

    def health_care(self):
        if self.is_student == True:
            return 0
        else:
            return self.salary * 0.05

    def email(self):
        return self.name[0].lower() + "." + self.surname[0].lower() + "@" + self.company.replace(' ', '.').lower() + ".com"


Kowalski = Pracownik("szef", 300000, "Jan", "Kowalski", 10, False)
Nowak = Pracownik("asystent", 5000, "Michał", "Nowak", 10, False)
Smith = Pracownik("stażysta", 2000, "John", "Smith", 0, True)

print(Kowalski.__dict__)
print(Kowalski.raises())
print(Kowalski.__dict__)
print("Taxes:", Kowalski.taxes())
print(Kowalski.email())