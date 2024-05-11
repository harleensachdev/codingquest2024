import requests
url = "https://codingquest.io/api/puzzledata?puzzle=28" 
response = requests.get(url)
if response.status_code == 200:
    input_data = response.text.splitlines()
else:
    print("Failed to retrieve input data. Status code:", response.status_code)

companies = {}
for entry in input_data:
    company, details = entry.split(": ")
    costtype, amount = details.split(" ")
    amount = int(amount)
    if company not in companies:
        companies[company] = 0
    if costtype in ["Seat", "Meals", "Luggage", "Fee", "Tax"]:
        companies[company] += amount
    elif costtype in ["Discount", "Rebate"]:
        companies[company] -= amount

final_costs = {}
for company, cost in companies.items():
    final_costs[company] = cost

cheapest_company = min(final_costs, key=final_costs.get)
cheapest_cost = final_costs[cheapest_company]

print("Cheapest option:", cheapest_company)
print("Final cost:", cheapest_cost)

# Answer: Cheapest option: CometAir, Final cost: $191274