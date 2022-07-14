from ensurepip import version
from termios import VERASE
from setuptools import setup, find_packages
from typing import list

PROJECT_NAME = "CEMENT_STRENGTH_PREDICTOR"
AUTHOR = "Abhishek Mhatre"
VERSION = "0.0.1"
DESRCIPTION= "This is a first FSDS Nov batch internship assignment"
REQUIREMENT_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list():
    with open(REQUIREMENT_FILE) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [module.replace("\n", "") for module in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        return requirements_list

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)