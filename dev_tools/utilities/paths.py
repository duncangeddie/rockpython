def run_paths_utility(command_parameter):
    #module imports
    from dev_tools.utilities.timestamp import generate_timestamp
    import json

    #cmd0 function
    cmd0 = str("load_base_directory")
    def load_base_directory():
        return '/home/duncan/Desktop/rockpython/dev_tools'

    #cmd1 function
    cmd1 = str("load_base_folders")
    def load_base_folders():
        os = __import__("os")
        base_directory = load_base_directory()
        base_folders_dict = {
            f: os.path.join(base_directory, f)
        for f in os.listdir(base_directory)
        if os.path.isdir(os.path.join(base_directory, f))
        }
        return base_folders_dict

    #cmd2 function
    cmd2 = str("print_base_folders")
    def print_base_folders():
        folders_dict = load_base_folders()
        for key, value in folders_dict.items():
            print(f"{key}:{value}")

    #cmd3 function
    cmd3 = str("export_base_folders")
    def export_base_folders():
        file_name = f"base_folders_{generate_timestamp()}.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/exports/"+"/"+export_name
        data = load_base_folders()
        try:
            with open(file_path,'w') as f:
                json.dump(data,f,indent=0)
        except FileNotFoundError:
            print("Error: The directory does not exist.")
        except PermissionError:
            print("Error: Permission denied when trying to write the file.")
        except TypeError as e:
            print(f"Error: Data contains non-serializable values. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    #process command
    commands = [cmd0,cmd1,cmd2,cmd3]
    command = str(command_parameter)

    #run command
    if command == cmd0:
        load_base_directory()
    elif command == cmd1:
        load_base_folders()
    elif command == cmd2:
        print_base_folders()
    elif command == cmd3:
        export_base_folders()
    else:
        print("⚠️ Error: Unknown command")

###TESTING CODE###
run_paths_utility("load_base_directory")
run_paths_utility("load_base_folders")
run_paths_utility("print_base_folders")
run_paths_utility("export_base_folders")
