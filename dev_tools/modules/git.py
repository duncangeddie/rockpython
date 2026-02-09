def run_git(command_parameter):
    # import packages
    from dev_tools.utilities.loader import run_loader
    modules = run_loader("import_py_packages")
    subprocess = modules["subprocess"]

    ## messages
    from dev_tools.utilities.messages import error_messages
    from dev_tools.utilities.messages import run_git_messages

#!#------------------------------------------------------------------
    # cmd0 function
    cmd0 = str("git_push")
    def run_git_push():
        run_git_messages("run_git_push")
        # user inputs commit message
        indent_quantity = int(1)
        indent = str("    "*indent_quantity)
        emoji_prefix = "⌨️"
        input_message = f"{indent}{emoji_prefix} Enter commit message: "
        commit_message = input(input_message)

        # commands for git workflow
        git_commands = [
            "git add .",
            f'git commit -m "{commit_message}"',
            "git push",
        ]

        # loop through the commands in list
        for cmd in git_commands:
            try:
                # run commands
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

#!#------------------------------------------------------------------
    # process command
    commands = [cmd0]
    command = str(command_parameter)

    # run command
    if command == cmd0:
        run_git_push()
    elif command == "":
        print("")
    else:
        print("⚠️ Error: Unknown command")

#!#------------------------------------------------------------------

### TESTING CODE ###
run_git("git_push")

