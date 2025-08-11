from setuptools import find_packages,setup
from typing import List

HYPEN_E = "-e."
def get_requirements(file_name:str)->List[str]:

    requirements=[]
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements



setup(
    name='project',
    version='0.0.1',
    author='Shreya',
    author_email='shreyasaxena117@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

    )