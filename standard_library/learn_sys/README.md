# sys

This module provides access to some **variables** used or maintained by the interpreter and to **functions** that interact strongly with the interpreter. Unless explicitly noted otherwise, all variables are read-only

## Common Variables and Functions

- `sys.argv`: list of command line arguments passed to a Python script. `argv[0]` is the script name
- `sys.exit([arg])`: raise a `SystemExit` exception, signaling an intention to exit the interpreter. `arg` can be an integer giving the exit status (defaulting to 0, indicate successful termination), or another type of object
- `sys.path`: a list of strings that specifies the search path for modules. Initialized from the environment variable `PYTHONPATH`, plus an installation-dependent default
- `sys.version`: a string containing the version number of the Python interpreter