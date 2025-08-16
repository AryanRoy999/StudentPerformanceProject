#this is the main setup file. in all the important files of this project you will find these comments to give you an idea and most accurate explanation of why and how a thing was done
#main motive of this file was to install all the requirements and a commented e is left in requirements file so that they can be updated when needed.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='AryanRoy999',
author_email='aryan09ashish@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)