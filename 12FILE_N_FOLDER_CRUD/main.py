from pathlib import Path
import os


def ReadFileNFolder():
    path = Path('')
    dirs = list(path.rglob('*'))
    for i, v in enumerate(dirs):
        print(f"{i+1}. {v}")


while(True):
    try:
        print('*** CHOOSE OPERATIONS YOU NEED TO PERFORM ***')
        print('1. ENTER FOLDER/DIRECTORY PATH TO BE CREATED.')
        print('2. READ All DIRECTORY & FILES.')
        print('3. ENTER FOLDER/DIRECTORY PATH TO BE UPDATED.')
        print('4. ENTER FOLDER/DIRECTORY PATH TO BE DELETED.')
        print('5. ENTER FILE PATH TO BE CREATED.')
        print('6. ENTER FILE PATH TO BE UPDATED.')
        print('7. ENTER FILE PATH TO BE DELETED.')
        print('0. EXIT APPLICATION.')
        n = int(input("Your Option: "))
        if n == 1:
            dirpath = input("ENTER DIRECTORY/FOLDER NAME: ")
            path = Path(dirpath)
            path.mkdir()
            print("OPERATION DONE SUCCESSFULLY!")
        elif n == 2:
            ReadFileNFolder()
            print("OPERATION DONE SUCCESSFULLY!")
        elif n == 3:
            ReadFileNFolder()
            dirpath = input("ENTER DIRECTORY/FOLDER NAME: ")
            path = Path(dirpath)
            path.rename(input("UPDATED DIRECTORY NAME: "))
            print("OPERATION DONE SUCCESSFULLY!")
        elif n == 4:
            ReadFileNFolder()
            dirpath = input("ENTER DIRECTORY/FOLDER NAME: ")
            path = Path(dirpath)
            dirs = list(path.rglob('*'))
            if len(dirs) > 0:
                confirm = input(
                    "directory is not empty, do you want to delete aferall ?(Y/N)")
                if confirm == 'y' or confirm == 'Y':
                    for i, v in enumerate(dirs):
                        if v.is_file():
                            os.remove(v)
                        else:
                            Path(v).rmdir()
            path.rmdir()
            print("OPERATION DONE SUCCESSFULLY!")
        elif n == 5:
            ReadFileNFolder()
            dirpath = input("ENTER FILE NAME WITH EXTENSION: ")
            path = Path(dirpath)
            if path.exists():
                print("FILE ALREADY EXISTS")
            else:
                with open(dirpath, 'w') as fw:
                    data = input(
                        "Enter New File Data(Press Enter to skip): ")
                    fw.write(data)
                print("OPERATION DONE SUCCESSFULLY!")
        elif n == 6:
            ReadFileNFolder()
            dirpath = input("ENTER FILE NAME WITH EXTENSION: ")
            path = Path(dirpath)
            print("1. TO RENAME FILE")
            print("2. TO APPEND FILE DATA")
            print("3. TO REPLACE FILE DATA")
            op = int(input("Enter renaming option: "))
            if op == 1:
                newfilename = input("RENAMED FILE NAME: ")
                p = Path(newfilename)
                if not p.exists():
                    os.rename(path, p)
                    print("OPERATION DONE SUCCESSFULLY!")
                else:
                    print("choose another path/name, choose again")
            elif op == 2:
                with open(dirpath, 'a') as fa:
                    data = input("Enter appending data: ")
                    fa.write(" " + data)
                    print("OPERATION DONE SUCCESSFULLY!")
            elif op == 3:
                with open(dirpath, 'w') as fw:
                    data = input("Enter replacing data: ")
                    fw.write(data)
                    print("OPERATION DONE SUCCESSFULLY!")
            else:
                print("RENAMiNG OPTION NOT FOUND, CHOOSE AGAIN")

        elif n == 7:
            ReadFileNFolder()
            dirpath = input("ENTER FILE NAME WITH EXTENSION: ")
            path = Path(dirpath)
            if path.exists():
                os.remove(path)
                print("OPERATION DONE SUCCESSFULLY!")
            else:
                print("404 - FINE NOT FOUND.")
        elif n == 0:
            print("EXITING APPLICATION")
            exit(0)
        else:
            print("MAKADE DEKH KR INPUT DAAL")

    except Exception as err:
        print(err)
