def show_main_menu():
    # module imports
    from .messages import error_messages

    # menu options
    menu0_command = "exit"
    menu0_description = "Exit dev_tools"

    menu1_command = "npm build production"
    menu1_description = "Build DDEV project with npm production build"

    menu2_command = "git push"
    menu2_description = "Push a commit to the git repo"

    # set a fixed width for the command column
    width = 25

    #menu options list
    menu_options = [
        f"{menu0_command.ljust(width)} {menu0_description}",
        f"{menu1_command.ljust(width)} {menu1_description}",
        f"{menu2_command.ljust(width)} {menu2_description}",
    ]

    #print out menu header
    print("-"*80)
    print("🖥️ rockpython/dev_tools")
    print("-"*80)

    #command label
    print("🔽 Commands ")
    print("-"*80)

    #print out menu options
    for option in menu_options:
        print(option)
    print("-"*80)

### TESTING CODE ###
#show_main_menu()

to_do = """
- Move menu_options to a config file with CRUD options
"""
