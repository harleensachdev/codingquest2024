import requests
url = "https://codingquest.io/api/puzzledata?puzzle=30" 
response = requests.get(url)
if response.status_code == 200:
    input_data = response.text.splitlines()
else:
    print("Failed to retrieve input data. Status code:", response.status_code)
data = []
for element in input_data:
    input_data = element.split()
for element in input_data:
    data.append(int(element))
print(input_data)

def parse_encoded_data(encoded_data):
    encoded_pairs = []
    for i, num in enumerate(encoded_data):
        if i % 2 == 0:
            value = 1
        else:
            value = 0
        encoded_pairs.append((num, value))

    return encoded_pairs

encoded_pairs= parse_encoded_data(data)
width = 80
height = 100

def create_image(encoded_pairs):
    image = [[''] * height for _ in range(width)] 
    x, y = 0, 0
    for count, value in encoded_pairs:
        if value == 1:
            symbol = '.' * count 
        else:
            symbol = '#' * count
        for s in symbol:
            image[x][y] = s
            y += 1
            if y == 100:
                y = 0
                x += 1

    return image

image = create_image(encoded_pairs)
for row in image:
    print(''.join(row))

