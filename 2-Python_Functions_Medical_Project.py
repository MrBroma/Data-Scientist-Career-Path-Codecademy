# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

# Estimate of our insurance cost 
loic_insurance_cost = calculate_insurance_cost(name = "Loic", age = 34, sex = 0, bmi = 26.2, num_of_children = 0, smoker = 0)

print(omar_insurance_cost)

# Extra_difference in costs
def difference_cost(cost1, cost2):
  diff = cost1 - cost2
  print(f"The difference in insurance cost is {cost1-cost2} dollars.")

difference = difference_cost(omar_insurance_cost,maria_insurance_cost)