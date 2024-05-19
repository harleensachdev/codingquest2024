import requests

url = "https://codingquest.io/api/puzzledata?puzzle=32"
response = requests.get(url)
if response.status_code == 200:
    data = response.text.splitlines()
else:
    print("Failed to retrieve input data. Status code:", response.status_code)
    exit()

rover_logs = []
cleaned_data = []

for line in data:
    if line.startswith("Rover"):
        route = line.split(": ")[1].split(" -> ")
        rover_logs.append(route)
    else:
        cleaned_data.append(line)

cleaned_data = [line for line in cleaned_data if line.strip()]
print(cleaned_data)
locations = cleaned_data[0].split()
print(locations)

distance_matrix = {}

for i in range(1, len(cleaned_data)):
    row = cleaned_data[i].split()
    start = row[0]
    for j in range(1, len(row)):
        end = locations[j - 1]
        distance_matrix[(start, end)] = int(row[j])

total_distance = 0
for route in rover_logs:
    rover_distance = 0
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        if (start, end) in distance_matrix:
            rover_distance += distance_matrix[(start, end)]
        else:
            print(f"Error: Distance from {start} to {end} not found in the distance matrix.")
    total_distance += rover_distance


print("Total distance traveled by all rovers:", total_distance)
