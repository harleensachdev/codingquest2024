import requests
import math
url = "https://codingquest.io/api/puzzledata?puzzle=31" 
response = requests.get(url)
if response.status_code == 200:
    data = response.text.splitlines()
else:
    print("Failed to retrieve input data. Status code:", response.status_code)
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
star_systems = []
index = 0
for line in data:
    if line == data[0]:
        continue
    components = line.split()
    star_name = " ".join(components[:-4])
    for component in components:
        if is_float(component) == True:
            index = components.index(component)
            if is_float(components[index+1]) == True:
                break
    
    x = float(components[index+1])
    y = float(components[index + 2])
    z = float(components[index + 3])
    star_systems.append((star_name, (x, y, z)))


def calculate_distance(coord1, coord2):
    xdiff = coord1[0] - coord2[0]
    ydiff = coord1[1] - coord2[1]
    zdiff = coord1[2] - coord2[2]
    distance = math.sqrt(xdiff**2 + ydiff**2 + zdiff**2)
    return distance

closest_pair = ()
min_distance = float('inf')
for i in range(len(star_systems)):
    for j in range(i+1, len(star_systems)):
        system1 = star_systems[i]
        system2 = star_systems[j]
        distance = calculate_distance(system1[1], system2[1])
        if distance<min_distance:
            min_distance = distance
            closest1 = system1[0]
            closest2 = system2[0]

print("Closest pair of star systems:", closest1,"and", closest2)
print("Distance:", round(min_distance, 3), "light years")

# Answer: Closest pair of star systems: Procyon A and Luyten's star
## Distance: 1.099 light years