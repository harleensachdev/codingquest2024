from collections import deque, defaultdict
input_data = """
0
taskmgr.exe 5065932
Customer_Feedback_Compilation_2024.xlsx 2646384
VLC-3.0.16-win64.exe 3971817
ProductLaunch2024.png 3712336
temporary_573 5048816
delete_708 2054307
temporary_023 [1]
1
Conference_Break_Music.mp3 5179931
SlackSetup-x64-4.3.2.exe 2384929
Strategic_Plans [2]
Client_Dinner_Mar_2024.jpeg 5364778
FileZilla_3.55.1_win64-setup.exe 4623628
Charity_Event_011524.HEIC 2134414
Office_Christmas_Party_2023.jpeg 687062
2
Product_Video_Soundtrack.aiff 813896
Operations_Manuals [3]
Signed_NDA_JohnDoe_021523.pdf 3257437
delete_930 9940460
Client_Acquisition_Strategies [4]
temporary_493 1332303
Marketing_Brochure_Image1.PSD 5913782
3
ProductLaunch2024.png 4396529
Motivational_Morning_Playlist.m3u 5619626
Network_Configuration_Settings.txt 1068226
CRM_Database_Export_021724.csv 5812973
Competitor_Analysis_0224.pdf 1088620
Employee_Training_Videos_Link.txt 267104
delete_530 7150742
4
temporary_751 1051994
delete_208 6042521
Logo_Rebrand_Options.svg 3438585
Node-v14.17.3-x64.msi 2056068
Expense_Report_Jan_2024.pdf 5775782
user32.dll 2371618
delete_027 9003131
"""

def parse_input(input_data):
    folder_data = defaultdict(list)
    lines = input_data.strip().split('\n')
    current_folder = None

    for line in lines:
        if line.isdigit():
            current_folder = int(line)
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
            if '[' in item:
                subfolder = int(item[item.find('[') + 1:item.find(']')])
                folder_name = item[:item.find('[')].strip()
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

folder_data = parse_input(input_data)
total_deletion_size = calculate_deletion_size(folder_data)
print(total_deletion_size)

