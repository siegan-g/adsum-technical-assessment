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


## Docs

- FastAPI generates OpenAPI docs on the fly, you can access the documentation via `localhost:8000/docs`

## CLI 

- A simple CLI tool is included for specific administrative functions,it can be called with the `opentax` command:

```sh
usage: opentax [-h] {seed} ...

OpenTax Backend CLI

positional arguments:
  {seed}      Available commands
    seed      Seed the database with sample data

options:
  -h, --help  show this help message and exit
```
### Seeding

- Call by running `opentax seed`

```sh
usage: opentax seed [-h] [--payments PAYMENTS] [--invoices INVOICES]

options:
  -h, --help           show this help message and exit
  --payments PAYMENTS  Number of payments to create (default: 30)
  --invoices INVOICES  Number of invoices to create (default: 30)
```
