from setuptools import setup, find_packages

setup(
    name="OpenTax", 
    version="1.0", 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'opentax=presentation.cli.main:main',
        ],
    },
)
