'''
    The setup.py file is an essential part of packaging and distributing Python projects.
    It is used by setuptools(or distutils in older Python versions) to define
    the configurations of your project, such as its metadata, dependecies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirements_list:List[str] = []
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_list

setup(
    name="Basic_Python",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
    author="Test",
    author_email="test@gmail.com",
    description="Your package description",
    url="https://github.com/yourusername/yourrepository",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)