# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker,):
  estimaded_cost = (250*age)+(128*sex)+(370*bmi)+(425*num_of_children)+(24000*smoker)-12500
  return estimaded_cost, print("The estimaded insurance cost for "+ name +" is "+str(estimaded_cost)+" dollars")

def dif_insurance_cost(cost1, cost2):
  dif = cost1 - cost2
  return dif, print("The difference in insurance cost is "+ str(dif) +" dollars.")

maria_insurance_cost =calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

my_insurance_cost = calculate_insurance_cost("Loic", 34, 1, 26, 0, 0)

omar_maria_diference = dif_insurance_cost(omar_insurance_cost[0], maria_insurance_cost[0])
