def run_build(command_parameter):
    # import packages
    from dev_tools.utilities.loader import run_loader
    modules = run_loader("import_py_packages")
    # assign the pacakges from the dictionary
    subprocess = modules["subprocess"]
    json = modules["json"]
    os = modules["os"]

    ## messages
    from dev_tools.utilities.messages import error_messages
    from dev_tools.utilities.messages import run_build_messages
#!#-------------------------------------------------------------------------
    # cmd0 function
    cmd0 = str("production_build")
    def run_production_build():
        # commands for production build
        build_commands = [
            "ddev start",
            "php artisan view:clear",
            "php artisan config:clear",
            "php artisan route:clear",
            "NODE_ENV=production npm run build",
            "ddev restart",
            "ddev launch",
        ]

        # loop through each command in the list
        run_build_messages("run_production_build")
        for cmd in build_commands:
            try:
                # 👉 this is where the command actually runs
                result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)

                # print command output
                if result.stdout.strip():
                    print(result.stdout)

                # print any errors
                if result.stderr.strip():
                    print(result.stderr)

            except subprocess.CalledProcessError as e:
                error_messages("subprocess_called")

                # print any output captured before error
                if e.stdout:
                    print(e.stdout)
                if e.stderr:
                    print(e.stderr)
#-------------------------------------------------------------------------
    # process command
    commands = [cmd0]
    command = str(command_parameter)

    # run command
    if command == cmd0:
        run_production_build()
    elif command == "":
        print("")
    else:
        print("⚠️ Error: Unknown command")

### TESTING CODE ###
run_build("production_build")
