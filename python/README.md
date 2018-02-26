# Python

## Virtual environments

To create and use virtual environments to make dependency management easier,
the following code can be used as a quickstart

```bash
# create the virtual environment (may not work with spaces in path)
python3 -m venv /path/to/folder

# activate the virtual environment
source /path/to/folder/bin/activate

# deactivate when finished
deactivate
```

The current python version can be checked with `python --version` and the 
current virtual environment should be prepended to the location in the
terminal window.
