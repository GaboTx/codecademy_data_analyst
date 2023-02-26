names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
for individual_price in actual_insurance_costs:
  total_cost =+ individual_price

average_cost = total_cost / len(actual_insurance_costs)

print("Average Insurance Cost: ",average_cost," dollars.")

for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for ",name, " is ", insurance_cost," dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost is above range")
  elif insurance_cost < average_cost:
    print("The insurance cost is below range")
  else:
    print("The insurance cost is equal range")
  print("---------------")

#The actual insurance cost is 10% higher than estimated list
updated_estimated_costs = [individual_cost*11/10 for individual_cost in estimated_insurance_costs]
for i in range(0, len(estimated_insurance_costs)):
  percentage_higher = ((actual_insurance_costs[i] - estimated_insurance_costs[i])/estimated_insurance_costs[i]) * 100
  
  print("Each actual cost is: ", percentage_higher,"% than estimated cost")

    
