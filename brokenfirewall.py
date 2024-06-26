import requests
url = "https://codingquest.io/api/puzzledata?puzzle=29" 
response = requests.get(url)
if response.status_code == 200:
    input_data = response.text.splitlines()
else:
    print("Failed to retrieve input data. Status code:", response.status_code)
totaldestination = 0
totalsource = 0
for string in input_data:
    length = 0
    stringdivided = []
    bytesdivided = []
    sourceipaddress =[]
    sipaddress = []
    destinationipaddress = []
    dipaddress = []

    for character in string:
        stringdivided.append(character)
    for i in range(0, len(string), 2):
        bytesdivided.append(string[i:i+2])
    length = ''.join(bytesdivided[2:4])
    length = int(length,16)

    sipaddress = bytesdivided[12:16]

    dipaddress = bytesdivided[16:20]

    for byte in sipaddress:
        sourceipaddress.append(int(byte,16))
    if sourceipaddress[0] == 192 and sourceipaddress[1] == 168:
        totalsource += length
    if sourceipaddress[0] == 10 and sourceipaddress[1] == 0:
        totaldestination += length

    for byte in dipaddress:
        destinationipaddress.append(int(byte,16))
    if destinationipaddress[0] == 10 and destinationipaddress[1] == 0:
        totaldestination += length
    if destinationipaddress[0] == 192 and destinationipaddress[1] == 168:
        totalsource += length

print(totaldestination)
print(totalsource)

# Answer: 258956/256237
