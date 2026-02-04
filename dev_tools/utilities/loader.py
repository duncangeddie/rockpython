def run_loader(command_parameter):
    #module imports
    import json

    #cmd0 function
    cmd0 = str("reset_python_packages")
    def reset_python_packages():
        data = ["json","os","subprocess","sys"]
        reset_name = "python_packages.json"
        reset_path = "/home/duncan/Desktop/rockpython/dev_tools/config/"+"/"+reset_name
        try:
            with open(reset_path,'w') as f:
                json.dump(data,f,indent=0)
        except FileNotFoundError:
            print("Error: The directory does not exist.")
        except PermissionError:
            print("Error: Permission denied when trying to write the file.")
        except TypeError as e:
            print(f"Error: Data contains non-serializable values. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    #cmd1 function
    cmd1 = str("import_python_packages")
    def import_python_packages():
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            imported_modules = {}
            for pkg in data:
                try:
                    imported_modules[pkg] = __import__(pkg)
                    print(f"Successfully imported {pkg}")
                except ImportError as e:
                    print(f"Failed to import {pkg}: {e}")
            return imported_modules

        except FileNotFoundError:
            print("Error: The file does not exist.")
        except PermissionError:
            print("Error: Permission denied when trying to read the file.")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    #cmd2 function
    cmd2 = str("print_python_packages")
    def print_python_packages():
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        try:
            with open(file_path,'r') as f:
                data = json.load(f)
                for item in data:
                    print(item)
        except FileNotFoundError:
            print("Error: The file does not exist.")
        except PermissionError:
            print("Error: Permission denied when trying to read the file.")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    #cmd3 function
    cmd3 = str("add_python_package")
    def add_python_package():
        print("add is WIP")

    #cmd4 function
    cmd4 = str("edit_python_package")
    def edit_python_package():
        print("edit is WIP")

    #cmd5 function
    cmd5 = str("delete_python_package")
    def delete_python_package():
        print("delete is WIP")

    #process command
    commands = [cmd0,cmd1,cmd2,cmd3,cmd4,cmd5]
    command = str(command_parameter)

    #run command
    if command == cmd0:
        reset_python_packages()
    elif command == cmd1:
        load_python_packages()
    elif command == cmd2:
        print_python_packages()
    elif command == cmd3:
        add_python_package()
    elif command == cmd4:
        edit_python_package()
    elif command == cmd5:
        delete_python_package()
    else:
        print("⚠️ Error: Unknown command")

#!#!#!#!#!#!# ADD LOAD AS A FUNCTION

###TESTING CODE###
#run_loader("reset_python_packages")
#run_loader("import_python_packages")
run_loader("print_python_packages")
#run_loader("add_python_package")
#run_loader("edit_python_package")
#run_loader("delete_python_package")
