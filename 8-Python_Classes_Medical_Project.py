class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + "’s estimated insurance costs is " + str(estimated_cost) + " dollars.")
  
  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child")
    else:
      print(self.name + " has " + str(self.num_of_children) + " children")
  
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
  def update_smoking_status(self, new_smoking_status):
    self.smoke = new_smoking_status

  def patient_profile(self):
    patient_information = {}
    patient_information["name"] = self.name
    patient_information["age"] = self.age
    patient_information["sex"] = self.sex
    patient_information["bmi"] = self.bmi
    patient_information["num_of_children"] = self.num_of_children
    patient_information["smoker"] = self.smoker
    return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient2 = Patient("Loic", 35, 1, 26, 0, 0)
# patient1.estimated_insurance_cost()
# patient1.update_age(26)
# patient1.estimated_insurance_cost()
# patient1.update_num_children(1)
# patient1.estimated_insurance_cost()

print(patient1.patient_profile())
print(patient2.patient_profile())
