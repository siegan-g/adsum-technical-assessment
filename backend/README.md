# Python - FastAPI Backend

## Setting up the development environment

### Requirements
- Python 3.13.7

1. Create a virtual environment:
   `python -m venv env`

2. Activate the virtual environment based on your Shell:
    Linux/Bash: `source env/bin/activate`
    Powershell : `./env/bin/Activate.ps1`

3. Install packages
   `pip install -r requirements.txt`

4. Install the project as a package to avoid import issues
   `pip install -e .`


### Notes 
- FastAPI/Uvicorn may install uvloop which does not support Windows; if you are developing on a Windows machine it should still run fine as it is an extra dependency to the framework