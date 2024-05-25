from collections import defaultdict, deque

def parse_input(input_data):
    folder_data = defaultdict(list)
    lines = input_data.strip().split('\n')
    current_folder = None

    for line in lines:
        if line.startswith('Folder:'):
            current_folder = int(line.split(':')[1].strip())
        else:
            folder_data[current_folder].append(line.strip())

    return folder_data

def calculate_deletion_size(folder_data):
    total_deletion_size = 0
    queue = deque([(0, False)])
    visited_folders = set()

    while queue:
        current, should_delete = queue.popleft()
        if current in visited_folders:
            continue

        visited_folders.add(current)

        for item in folder_data[current]:
            if '[FOLDER ' in item:
                subfolder = int(item[item.find('[FOLDER ') + 8:item.find(']')])
                folder_name = item[:item.find('[FOLDER ')].strip()
                if 'delete' in folder_name.lower() or 'temporary' in folder_name.lower() or should_delete:
                    queue.append((subfolder, True))
                else:
                    queue.append((subfolder, False))
            else:
                file_name, size = item.rsplit(' ', 1)
                size = int(size)
                if 'delete' in file_name.lower() or 'temporary' in file_name.lower() or should_delete:
                    total_deletion_size += size

    return total_deletion_size


import requests
import math
url = "https://codingquest.io/2024/day07_files_to_scan.txt" 
response = requests.get(url)
if response.status_code == 200:
    input_data = response.text
else:
    print("Failed to retrieve input data. Status code:", response.status_code) 

folder_data = parse_input(input_data)
total_deletion_size = calculate_deletion_size(folder_data)
print(total_deletion_size)
