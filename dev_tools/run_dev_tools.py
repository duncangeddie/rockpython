#import modules
from dev_tools.utilities.loader import run_loader
modules = run_loader("import_py_packages")
for name, module in modules.items():
    globals()[name] = module  # safer than locals()

#import utilities
from dev_tools.utilities.menus import show_main_menu
from dev_tools.modules.npm_build import run_build
from dev_tools.modules.git import run_git

#open app loop
while True:
    #load main menu
    show_main_menu()
    user_option_input = input("//")
    print("-"*80)
    command = user_option_input.lower()

    #run command
    if command == "exit":
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif command == "npm build production":
        run_build("production_build")
    elif command == "git push":
        run_git("git_push")
    else:
        print("ERROR MESSAGE HERE")

    #clear terminal after command runs
    os.system("cls" if os.name == "nt" else "clear")

