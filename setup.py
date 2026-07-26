from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # FIX: Use .strip() to remove all hidden whitespaces and newlines completely
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='Math_Score_Predictor',
    version='0.1.0',
    author='Noman',
    author_email='abdullahcse.cou14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
