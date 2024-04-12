import os

folder_list = input("Enter the folder names with space : ").split()

for folder in folder_list:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, this folder does not exist : " + folder)
        break
    except PermissionError:
        break
        print("No access to this folder : " + folder)
        
    print("** Files present under folder : " + folder)
    for file in files:
        print(file)
