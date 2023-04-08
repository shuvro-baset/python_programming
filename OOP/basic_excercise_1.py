class Vaccine:
    def __init__(self, name, md_in, intrvl):
        self.name = name
        self.md_in = md_in
        self.intrvl = intrvl


class Person:
    def __init__(self, p_name, p_age, p_type="General Citizen"):
        self.p_name = p_name
        self.p_age = p_age
        self.p_type = p_type
        self.vac = ""
        self.first_dose = False
        self.second_dose = False

    def pushVaccine(self, vacN, dose="first_dose"):
        if dose == "first_dose":
            if self.p_age >= 25 or self.p_type == "Student":
                self.vac = vacN
                self.first_dose = True
                print("1st dose done for ", self.p_name)
            else:
                print("Sorry", self.p_name, ", Minimum age for taking vaccine is 25 year now.")
        elif self.first_dose == True:
            if self.vac.name != vacN.name:
                print("Sorry", self.p_name, ", you can't take 2 different vaccines")
            else:
                self.second_dose = True
                print("2nd dose done for", self.p_name)

    def showDetail(self):
        print("Name: ", self.p_name, "Age: ", self.p_age, "Type: ", self.p_type)
        print("Vaccine Name: ", self.vac.name)
        if self.second_dose:
            print("1st dose: Given")
            print("2nd dose: Given")
        else:
            print("1st dose: given")
            print("2nd dose: ", "please come after", self.vac.intrvl, "days")


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopherm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("===========")
p1.pushVaccine(astra)
print("===========")
p1.showDetail()
print("===========")
p1.pushVaccine(sin, "2nd Dose")
print("===========")
p1.pushVaccine(astra, "2nd Dose")
print("===========")
p1.showDetail()
print("===========")
p2 = Person("Carol", 23, "Actor")
print("===========")
p2.pushVaccine(sin)
print("===========")
p3 = Person("David", 34)
print("===========")
p3.pushVaccine(modr)
print("===========")
p3.showDetail()
print("===========")
p3.pushVaccine(modr, "2nd dose")
