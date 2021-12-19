medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# Working with Strings
# print(medical_data)
updated_medical_data = medical_data.replace('#', '$')
# print(updated_medical_data)

num_records = 0
for char in updated_medical_data:
  if char == '$':
    num_records += 1

#print('There are ' + str(num_records) + ' medical records in data')

# Splitting Strings
medical_data_split = updated_medical_data.split(';')
# print(medical_data_split)

medical_records = []
for data in medical_data_split:
  medical_records.append(data.split(","))
# print(medical_records)

# Cleaning Data
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
#print(medical_records_clean)

# Analyzing Data
for record in medical_records_clean:
  record[0] = record[0].upper()
  # print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  # append the name, age, BMI, and insurance cost from the current medical record
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))
  
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
# print(total_bmi)
print()
average_bmi = round(total_bmi/len(bmis), 2)
# print('Average BMI: ' + str(average_bmi))

# Suppress dollars symbol in insurance_costs
insurance_costs_clean = []
total_costs = 0
for costs in insurance_costs:
  insurance_costs_clean.append(costs.strip('$'))
  for cost_clean in insurance_costs_clean:
    total_costs += float(cost_clean)
    average_insurance_costs = total_costs / (len(insurance_costs))
print(total_costs)
print()
print('The average insurance cost is $' + str(average_insurance_costs))
print()

# Print informations for each person in the list
for i in range(len(names)):
  sentence = "{name} is {age} years old with a BMI of {bmi} and an insurance cost of {insurance_cost}."
  print(sentence.format(name=names[i], age=ages[i], bmi=bmis[i], insurance_cost=insurance_costs[i]))