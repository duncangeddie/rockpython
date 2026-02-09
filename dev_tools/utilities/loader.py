def run_loader(command_parameter):
    #module imports
    import json
    ##messages
    from .messages import error_messages
    from .messages import loader_messages
    from .messages import json_messages

#!#-------------------------------------------------------------------------
    #cmd0 function
    cmd0 = str("reset_py_packages")
    def reset_py_packages():
        loader_messages("reset_py_packages")
        #define base data and file path
        data = ["json","os","subprocess","sys"]
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/"+file_name
        try:
            json_messages("saving_json",file_name)
            with open(file_path,'w') as f:
                json.dump(data,f,indent=0)
                json_messages("saved_json",file_name)
        #error exceptions for file dump
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except TypeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #cmd1 function
    cmd1 = str("load_py_packages")
    def load_py_packages():
        loader_messages("load_py_packages")
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #load json list
        try:
            #json_messages("loading_json",file_name)
            with open(file_path,'r') as f:
                data = json.load(f)
                #json_messages("loaded_json",file_name)
        #error exceptions for file dump
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except json.JSONDecodeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")
        #return loaded data
        return data
#!#-------------------------------------------------------------------------
    #cmd2 function
    cmd2 = str("import_py_packages")
    def import_py_packages():
        #loader_messages("import_py_packages")
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #load json list and import packages with import error exceptions
        try:
            #json_messages("loading_json",file_name)
            with open(file_path, 'r') as f:
                data = json.load(f)
            imported_modules = {}
            for pkg in data:
                try:
                    imported_modules[pkg] = __import__(pkg)
                    emoji_prefix = str("📦")
                    indent_quantity = int(2)
                    indent = str("    "*indent_quantity)
                    #print(f"{indent}{emoji_prefix} Successfully imported {pkg}")
                except ImportError as e:
                    emoji_prefix = str("❌")
                    indent_quantity = int(2)
                    indent = str("    "*indent_quantity)
                    #print(f"{indent}{emoji_prefix} Failed to import {pkg}: {e}")
            return imported_modules
        #error exceptions for file load
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except json.JSONDecodeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #cmd3 function
    cmd3 = str("print_py_packages")
    def print_py_packages():
        loader_messages("print_py_packages")
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #load json list and print packages listed
        try:
            json_messages("loading_json",file_name)
            with open(file_path,'r') as f:
                data = json.load(f)
                for item in data:
                    emoji_prefix = str("📦")
                    indent_quantity = int(2)
                    indent = str("    "*indent_quantity)
                    message = str(f"{indent}{emoji_prefix} {item}")
                    print(message)
        #error exceptions for file load
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except json.JSONDecodeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #cmd4 function
    cmd4 = str("add_py_package")
    def add_py_package():
        loader_messages("adding_py_package")
        #load json list as variable
        data = load_py_packages()
        #user enters name of new package
        emoji_prefix = str("⌨️")
        input_indent_quantity = int(1)
        input_indent = str("    "*input_indent_quantity)
        input_message = str(f"{input_indent}{emoji_prefix} Enter package name to add: ")
        add = str(input(input_message))
        #add new package to list
        data.append(add)
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #dump updated list to json
        try:
            json_messages("saving_json",file_name)
            with open(file_path,'w') as f:
                json.dump(data,f,indent=0)
                json_messages("saved_json",file_name)
        #error exceptions for file dump
        except FileNotFoundError:
            error_messages("file_not_found")
        except PermissionError:
            error_messages("permission_denied")
        except TypeError as e:
            error_messages("type")
        except Exception as e:
            print({e})
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #cmd5 function
    cmd5 = str("edit_py_package")
    def edit_py_package():
        loader_messages("edit_py_package")
        #load json list as variable
        data = load_py_packages()
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #enter index number of list item
        emoji_prefix = str("⌨️")
        input_indent_quantity = int(1)
        input_indent = str("    "*input_indent_quantity)
        input_message = str(f"{input_indent}{emoji_prefix} Enter package name to edit: ")
        edit_ref = str(input(input_message))
        #search data to check if package exists
        if edit_ref in data:
            exist_query = True
        else:
            exist_query = False
        #edit and dump file if package exists
        if exist_query == True:
            emoji_prefix = str("📦")
            indent_quantity = int(1)
            indent = str("    "*input_indent_quantity)
            message = str(f"{indent}{emoji_prefix} {edit_ref} found")
            print(message)
            input_indent_quantity = int(1)
            input_indent = str("    "*input_indent_quantity)
            input_message = str(f"{input_indent}{emoji_prefix} Enter new name for package: ")
            edit_str = str(input(input_message))
            #find index number of item and edit
            edit_index = data.index(edit_ref)
            data[edit_index] = edit_str
            #dump updated list to json
            try:
                json_messages("saving_json",file_name)
                with open(file_path,'w') as f:
                    json.dump(data,f,indent=0)
                    json_messages("saved_json",file_name)
            #error exceptions for file dump
            except FileNotFoundError:
                error_messages("file_not_found")
            except PermissionError:
                error_messages("permission_denied")
            except TypeError as e:
                error_messages("type")
            except Exception as e:
                print({e})
                error_messages("unexpected")

        else:
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #cmd6 function
    cmd6 = str("delete_py_package")
    def delete_py_package():
        loader_messages("delete_py_package")
        #load json list as variable
        data = load_py_packages()
        #define file path
        file_name = "python_packages.json"
        file_path = "/home/duncan/Desktop/rockpython/dev_tools/config/" + file_name
        #enter index number of list item
        emoji_prefix = str("⌨️")
        input_indent_quantity = int(1)
        input_indent = str("    "*input_indent_quantity)
        input_message = str(f"{input_indent}{emoji_prefix} Enter package to delete: ")
        delete_ref = str(input(input_message))
        #search data to check if package exists
        if delete_ref in data:
            exist_query = True
        else:
            exist_query = False
        #delete and dump file if package exists
        if exist_query == True:
            #find index number of item and delete
            delete_index = data.index(delete_ref)
            data.remove(delete_ref)
            emoji_prefix = str("🗑️")
            indent_quantity = int(1)
            indent = str("    "*input_indent_quantity)
            message = str(f"{indent}{emoji_prefix} {delete_ref} deleted from list")
            print(message)
            #dump updated list to json
            try:
                json_messages("saving_json",file_name)
                with open(file_path,'w') as f:
                    json.dump(data,f,indent=0)
                    json_messages("saved_json",file_name)
            #error exceptions for file dump
            except FileNotFoundError:
                error_messages("file_not_found")
            except PermissionError:
                error_messages("permission_denied")
            except TypeError as e:
                error_messages("type")
            except Exception as e:
                print({e})
                error_messages("unexpected")

        else:
            error_messages("unexpected")
#!#-------------------------------------------------------------------------
    #process command
    commands = [cmd0,cmd1,cmd2,cmd3,cmd4,cmd5,cmd6]
    command = str(command_parameter)

    #run command
    if command == cmd0:
        reset_py_packages()
    elif command == cmd1:
        return load_py_packages()
    elif command == cmd2:
        return import_py_packages()
    elif command == cmd3:
        print_py_packages()
    elif command == cmd4:
        add_py_package()
    elif command == cmd5:
        edit_py_package()
    elif command == cmd6:
        delete_py_package()
    else:
        print("⚠️ Error: Unknown command")
#!#-------------------------------------------------------------------------
###TESTING CODE###
#run_loader("reset_py_packages") #TESTED 05/02/2026
#run_loader("load_py_packages") #TESTED 05/02/2026
#run_loader("import_py_packages") #TESTED 05/02/2026
#run_loader("print_py_packages") #TESTED 05/02/2026
#run_loader("add_py_package") #TESTED 05/02/2026
#run_loader("edit_py_package") #TESTED 05/02/2026
#run_loader("delete_py_package") #TESTED 05/02/2026
#!#-------------------------------------------------------------------------
