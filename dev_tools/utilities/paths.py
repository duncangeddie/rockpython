def run_paths_utility(command_parameter):
    #module imports
    from dev_tools.utilities.timestamp import generate_timestamp
    import json
    ##messages
    from .messages import error_messages
    from .messages import paths_messages
    from .messages import json_messages

    #cmd0 function
    cmd0 = str("load_base_directory")
    def load_base_directory():
        paths_messages("load_base_directory")
        return '/home/duncan/Desktop/rockpython/dev_tools'

    #cmd1 function
    cmd1 = str("load_base_folders")
    def load_base_folders():
        os = __import__("os")
        base_directory = load_base_directory()
        paths_messages("load_base_folders")
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
        paths_messages("print_base_folders")
        for key, value in folders_dict.items():
            emoji_prefix = str("📂")
            indent_quantity = int(1)
            indent = str("    "*indent_quantity)
            print(f"{indent}{emoji_prefix} {key}:{value}")

    #cmd3 function
    cmd3 = str("export_base_folders")
    def export_base_folders():
        file_name = f"base_folders_{generate_timestamp()}.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/exports/"+"/"+file_name
        data = load_base_folders()
        try:
            json_messages("saving_json",file_name)
            with open(file_path,'w') as f:
                json.dump(data,f,indent=0)
                json_messages("saved_json",file_name)
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except TypeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")

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
#run_paths_utility("load_base_directory") #TESTED 09/02/2026
#run_paths_utility("load_base_folders") #TESTED 09/02/2026
#run_paths_utility("print_base_folders") #TESTED 09/02/2026
#run_paths_utility("export_base_folders") #TESTD 09/02/2026
