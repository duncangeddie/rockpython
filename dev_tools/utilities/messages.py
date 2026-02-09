def loader_messages(command_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "reset_py_packages": #cmd0
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Resetting python packages list to default")
        print(message)
    elif command == "load_py_packages": #cmd1
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Loading py packages")
        print(message)
    elif command == "import_py_packages": #cmd2
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Importing py packages")
        print(message)

    elif command == "print_py_packages": #cmd3
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Printing py packages")
        print(message)

    elif command == "adding_py_package": #cmd4
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Adding py package")
        print(message)

    elif command == "edit_py_package": #cmd5
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Editing py package")
        print(message)

    elif command == "delete_py_package": #cmd6
        emoji_prefix = str("⚙️")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Deleting py package")
        print(message)

    else:
        return None

#!#------------------------------------------------------------------
def error_messages(command_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "file_not_found":
        emoji_prefix = str("⚠️")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Error: File not found")
        print(message)
    elif command == "permission_denied":
        emoji_prefix = str("⚠️")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Error: Permission denied")
        print(message)
    elif command == "type":
        emoji_prefix = str("⚠️")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Error: Data type")
        print(message)
    elif command == "unexpected":
        emoji_prefix = str("⚠️")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Error: Unexpected")
        print(message)
    elif command == "subprocess_called":
        emoji_prefix = str("⚠️")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{emoji_prefix} Error: Subprocess called")
    else:
        return None

#!#------------------------------------------------------------------
def json_messages(command_parameter,file_name_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "loading_json":
        file_name = str(file_name_parameter)
        emoji_prefix = str("📂")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Loading {file_name}")
        print(message)
    elif command == "loaded_json":
        file_name = str(file_name_parameter)
        emoji_prefix = str("✅")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Loaded {file_name}")
        print(message)
    elif command == "saving_json":
        file_name = str(file_name_parameter)
        emoji_prefix = str("💾")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Saving {file_name}")
        print(message)
    elif command == "saved_json":
        file_name = str(file_name_parameter)
        emoji_prefix = str("✅")
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Saved {file_name}")
        print(message)
    else:
        return None

#!#------------------------------------------------------------------
def paths_messages(command_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "load_base_directory":
        emoji_prefix = str("⚙")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Loading base directory")
        print(message)
    elif command == "load_base_folders": #cmd1
        emoji_prefix = str("⚙")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Loading folder structures")
        print(message)
    elif command == "print_base_folders": #cmd2
        emoji_prefix = str("⚙")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Printing base folders")
        print(message)
    else:
        return None

#!#------------------------------------------------------------------
def run_build_messages(command_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "run_production_build":
        emoji_prefix = str("⚙")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Running production build")
        print(message)
    else:
        return None

#!#------------------------------------------------------------------
def run_git_messages(command_parameter):
    #process command
    command = str(command_parameter)

    #run command
    if command == "run_git_push":
        emoji_prefix = str("⚙")
        indent_quantity = int(0)
        indent = str("    "*indent_quantity)
        message = str(f"{indent}{emoji_prefix} Run git push")
        print(message)
    else:
        return None

#!#------------------------------------------------------------------

###TESTING CODE###

#Run git messages
run_git_messages("run_git_push")

#Run build messages
"""
run_build_messages("run_production_build")
"""

#Paths messages
"""
paths_messages("load_base_directory") #TESTED 09/02/2026
paths_messages("load_base_folders") #TESTED 09/02/2026
paths_messages("print_base_folders") #TESTED 09/02/2026
"""
#Loader messages
"""
loader_messages("reset_py_packages") #TESTED 05/02/2026
loader_messages("load_py_packages") #TESTED 05/02/2026
loader_messages("import_py_packages") #TESTED 05/02/2026
loader_messages("print_py_packages") #TESTED 05/02/2026
loader_messages("adding_py_package") #TESTED 05/02/2026
loader_messages("edit_py_package") #TESTED 05/02/2026
loader_messages("delete_py_package") #TESTED 05/02/2026
"""

#Error messages
"""
error_messages("file_not_found") #TESTED 05/02/2026
error_messages("permission_denied") #TESTED 05/02/2026
error_messages("type") #TESTED 05/02/2026
error_messages("unexpected") #TESTED 05/02/2026
"""

#JSON messages
"""
json_messages("loading_json", "test.json") #TESTED 05/02/2026
json_messages("loaded_json", "test.json") #TESTED 05/02/2026
json_messages("saving_json", "test.json") #TESTED 05/02/2026
json_messages("saved_json", "test.json") #TESTED 05/02/2026
"""
